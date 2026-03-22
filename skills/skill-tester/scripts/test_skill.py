#!/usr/bin/env python3
"""
LLM Skill Tester - Testa prompts contra LLM.

Roda dois tipos de teste:
1. DETERMINISTICO - Verifica patterns (emojis, salary, estrutura)
2. QUALITATIVO - LLM julga qualidade do prompt

Usage:
    python test_skill.py --project lovel --skill hunting
    python test_skill.py --project lovel --skill hunting --verbose
    python test_skill.py --project lovel --skill hunting --assess
    python test_skill.py --project lovel --all
    python test_skill.py --project lovel --all --assess
"""

import argparse
import json
import re
import subprocess
import sys
import time
import statistics
from pathlib import Path
from typing import Dict, List, Any, Optional

ROOT = Path(__file__).resolve().parent.parent.parent.parent

try:
    import requests
except ImportError:
    print("ERRO: requests não instalado")
    sys.exit(1)

COST_PER_1M_TOKENS = 3.0

_config = {
    "session_id": None,
    "total_tokens": 0,
    "total_cost": 0.0,
}


def reset_stats():
    _config["total_tokens"] = 0
    _config["total_cost"] = 0.0


def call_llm(prompt: str) -> dict:
    """Execute LLM call via OpenCode."""
    try:
        if _config.get("session_id") is None:
            resp = requests.post(
                "http://127.0.0.1:4096/session",
                json={"title": "skill-test"},
                timeout=10
            )
            _config["session_id"] = resp.json()["id"]
        
        session_id = _config["session_id"]
        t0 = time.time()
        
        message_resp = requests.post(
            f"http://127.0.0.1:4096/session/{session_id}/message",
            json={"parts": [{"type": "text", "text": prompt}]},
            timeout=120
        )
        
        latency = int((time.time() - t0) * 1000)
        
        if message_resp.status_code != 200:
            return {"error": message_resp.text, "output": "", "tokens": 0, "latency": latency}
        
        parts = message_resp.json().get("parts", [])
        output = ""
        for part in parts:
            if part.get("type") == "text":
                output = part.get("text", "")
                break
        
        return {"output": output.strip(), "tokens": 0, "latency": latency, "error": None}
    except Exception as e:
        return {"error": str(e), "output": "", "tokens": 0, "latency": 0}


def find_projects() -> List[str]:
    projects_dir = ROOT / "projects"
    if not projects_dir.exists():
        return []
    return [p.name for p in projects_dir.iterdir() if p.is_dir()]


def find_skills(project: str) -> List[str]:
    project_dir = ROOT / "projects" / project / "skills"
    skills = []
    if not project_dir.exists():
        return skills
    for platform in ["claude", "chatgpt"]:
        platform_dir = project_dir / platform
        if platform_dir.exists():
            for item in platform_dir.iterdir():
                if item.name.startswith("."):
                    continue
                if item.is_dir():
                    skills.append(item.name)
                elif item.suffix == ".md" and item.stem.startswith("skill_"):
                    skills.append(item.stem.replace("skill_", ""))
    return list(set(skills))


def find_skill_prompt(project: str, skill: str) -> Optional[Dict[str, str]]:
    project_dir = ROOT / "projects" / project / "skills"
    results: Dict[str, str] = {}
    for platform in ["claude", "chatgpt"]:
        if platform == "claude":
            skill_file = project_dir / platform / skill / "SKILL.md"
        else:
            skill_file = project_dir / platform / f"skill_{skill}.md"
        if not skill_file.exists() and platform == "chatgpt":
            skill_dir = project_dir / platform / skill
            if skill_dir.is_dir():
                skill_file = skill_dir / "SKILL.md"
        if skill_file.exists():
            results[platform] = skill_file.read_text()
    return results if results else None


def find_fixtures(project: str, skill: str) -> Optional[Path]:
    project_dir = ROOT / "projects" / project / "skills"
    for platform in ["claude", "chatgpt"]:
        fixtures_file = project_dir / platform / skill / "evals" / "testes.cue"
        if fixtures_file.exists():
            return fixtures_file
    return None


def load_cue_fixtures(fixtures_file: Path) -> Dict[str, Any]:
    try:
        result = subprocess.run(
            ["cue", "export", "--out", "json", str(fixtures_file)],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            return json.loads(result.stdout)
        return {"error": result.stderr[:300]}
    except Exception as e:
        return {"error": str(e)}


def grade_hunting(prompt: str, output: str) -> Dict[str, Any]:
    issues = []
    checks = {}
    
    has_emoji = bool(re.search(r"[\U0001F300-\U0001FAFF]", output))
    checks["no_emoji"] = not has_emoji
    if has_emoji:
        issues.append("Contém emoji")
    
    for section in ["ICP", "Salary", "Query", "X-Ray", "NOT"]:
        has_section = bool(re.search(rf"(?i)##\s*{section}", output))
        checks[f"has_{section.lower()}"] = has_section
        if not has_section:
            issues.append(f"Falta ## {section}")
    
    has_linkedin = bool(re.search(r"site:linkedin.com/in", output))
    checks["has_linkedin"] = has_linkedin
    if not has_linkedin:
        issues.append("X-Ray sem site:linkedin.com/in")
    
    salary_format = bool(re.search(r"R\$\s*\d+k?\s*[-–]\s*R\$\s*\d+k?", output))
    checks["salary_format"] = salary_format
    if not salary_format:
        issues.append("Salary sem formato R$ Xk – R$ Yk")
    
    synonyms = re.findall(r'\(([^)]+)\)', output)
    has_5plus = any(len([s.strip() for s in syn.split("OR") if s.strip()]) >= 5 for syn in synonyms)
    checks["min_synonyms"] = has_5plus
    if not has_5plus and synonyms:
        issues.append("Nenhum grupo com 5+ sinônimos")
    
    passed = sum(1 for v in checks.values() if v)
    score = round((passed / len(checks)) * 10, 1) if checks else 0
    
    return {"score": score, "passed": score >= 7.0, "checks": checks, "issues": issues}


def grade_outreach(prompt: str, output: str) -> Dict[str, Any]:
    issues = []
    checks = {}
    
    prompt_upper = prompt.upper()
    is_m1 = "M1" in prompt_upper or not any(x in prompt_upper for x in ["M2", "FOLLOW"])
    is_m2 = "M2" in prompt_upper
    is_followup = "FOLLOW" in prompt_upper or "DAY 4" in prompt_upper or "DAY 7" in prompt_upper
    
    if is_m1:
        m1_text = re.sub(r"(?i)^M1:?\s*", "", output).strip()
        checks["m1_200chars"] = len(m1_text) <= 200
        if len(m1_text) > 200:
            issues.append(f"M1 com {len(m1_text)} chars")
    
    if is_m2:
        has_salary = bool(re.search(r"R\$\s*\d+k?\s*[-–]\s*R\$\s*\d+k?", output))
        checks["salary_m2"] = has_salary
        if not has_salary:
            issues.append("M2 sem salary")
        
        has_invite = bool(re.search(r"invite=caroline\.lima798", output))
        checks["has_invite"] = has_invite
        if not has_invite:
            issues.append("Falta invite")
    
    if is_followup:
        has_followup = bool(re.search(r"(?i)(day\s*4|day\s*7)", output))
        checks["has_followup"] = has_followup
        if not has_followup:
            issues.append("Falta follow-up day 4/7")
    
    emoji_count = len(re.findall(r"[\U0001F300-\U0001FAFF]", output))
    checks["max_1_emoji"] = emoji_count <= 1
    if emoji_count > 1:
        issues.append(f"Muitos emojis ({emoji_count})")
    
    passed = sum(1 for v in checks.values() if v)
    score = round((passed / len(checks)) * 10, 1) if checks else 0
    
    return {"score": score, "passed": score >= 7.0, "checks": checks, "issues": issues}


def grade_post(prompt: str, output: str) -> Dict[str, Any]:
    issues = []
    checks = {}
    
    has_salary = bool(re.search(r"R\$\s*\d+k?\s*[-–]\s*R\$\s*\d+k?", output))
    checks["has_salary"] = has_salary
    if not has_salary:
        issues.append("Post sem salary")
    
    has_90dias = bool(re.search(r"(?i)90\s*dias", output))
    checks["has_90dias"] = has_90dias
    if not has_90dias:
        issues.append("Falta hook com 90 dias")
    
    has_invite = bool(re.search(r"invite=caroline\.lima798", output))
    checks["has_invite"] = has_invite
    if not has_invite:
        issues.append("Falta invite")
    
    has_emdash = bool(re.search(r"—", output))
    checks["no_emdash"] = not has_emdash
    if has_emdash:
        issues.append("Contém em-dash")
    
    passed = sum(1 for v in checks.values() if v)
    score = round((passed / len(checks)) * 10, 1) if checks else 0
    
    return {"score": score, "passed": score >= 7.0, "checks": checks, "issues": issues}


def grade_parecer(prompt: str, output: str) -> Dict[str, Any]:
    issues = []
    checks = {}
    
    has_resumo = bool(re.search(r"(?i)(resumo|perfil)", output))
    checks["has_resumo"] = has_resumo
    if not has_resumo:
        issues.append("Falta resumo")
    
    has_stack = bool(re.search(r"(?i)(stack|tecnologias)", output))
    checks["has_stack"] = has_stack
    if not has_stack:
        issues.append("Falta stack")
    
    has_pontos = bool(re.search(r"(?i)(pontos\s*(fortes|aten))", output))
    checks["has_pontos"] = has_pontos
    if not has_pontos:
        issues.append("Falta pontos")
    
    has_recomendacao = bool(re.search(r"(?i)(recomend|avanc)", output))
    checks["has_recomendacao"] = has_recomendacao
    if not has_recomendacao:
        issues.append("Falta recomendação")
    
    passed = sum(1 for v in checks.values() if v)
    score = round((passed / len(checks)) * 10, 1) if checks else 0
    
    return {"score": score, "passed": score >= 7.0, "checks": checks, "issues": issues}


GRADERS = {
    "hunting": grade_hunting,
    "outreach": grade_outreach,
    "post": grade_post,
    "parecer": grade_parecer,
}


def test_skill(project: str, skill: str, verbose: bool = False) -> Dict[str, Any]:
    """Testa uma skill com LLM."""
    _config["session_id"] = None
    results = {"project": project, "skill": skill, "platforms": {}, "summary": {}}
    
    prompts = find_skill_prompt(project, skill)
    if not prompts:
        return {"error": f"Skill '{skill}' não encontrada"}
    
    fixtures = find_fixtures(project, skill)
    if not fixtures:
        return {"error": f"Fixtures não encontrados"}
    
    data = load_cue_fixtures(fixtures)
    if "error" in data:
        return {"error": data["error"]}
    
    testes = data.get("testes", [])
    if not testes:
        return {"error": "Nenhum teste"}
    
    grader = GRADERS.get(skill)
    if not grader:
        return {"error": f"Grader não implementado"}
    
    reset_stats()
    
    for platform, prompt_template in prompts.items():
        platform_results = []
        
        if verbose:
            print(f"\n  Platform: {platform}")
        
        for i, test in enumerate(testes):
            test_id = test.get("id", i + 1)
            test_input = test.get("prompt", "")
            full_prompt = f"{prompt_template}\n\n---\n\nInput: {test_input}"
            
            if verbose:
                print(f"    Test {test_id}...")
            
            start = time.time()
            llm_resp = call_llm(full_prompt)
            latency = int((time.time() - start) * 1000)
            
            if llm_resp.get("error"):
                platform_results.append({
                    "test_id": test_id, "passed": False, "score": 0,
                    "error": llm_resp["error"], "latency_ms": latency
                })
                continue
            
            grading = grader(test_input, llm_resp["output"])
            platform_results.append({
                "test_id": test_id,
                "passed": grading["passed"],
                "score": grading["score"],
                "latency_ms": latency,
                "issues": grading["issues"]
            })
        
        scores = [r["score"] for r in platform_results if "score" in r]
        passed = sum(1 for r in platform_results if r.get("passed"))
        total = len(platform_results)
        
        results["platforms"][platform] = {
            "results": platform_results,
            "avg_score": round(statistics.mean(scores), 1) if scores else 0,
            "pass_rate": f"{passed}/{total}",
            "latency_ms": sum(r.get("latency_ms", 0) for r in platform_results)
        }
    
    all_scores = [r["avg_score"] for r in results["platforms"].values()]
    results["summary"] = {
        "avg_score": round(statistics.mean(all_scores), 1) if all_scores else 0,
        "pass_rate": f"{sum(int(r['pass_rate'].split('/')[0]) for r in results['platforms'].values())}/{sum(int(r['pass_rate'].split('/')[1]) for r in results['platforms'].values())}"
    }
    
    return results


def main():
    _config["session_id"] = None  # Reset session
    
    parser = argparse.ArgumentParser(description="LLM Skill Tester")
    parser.add_argument("--project", "-p", help="Nome do projeto")
    parser.add_argument("--skill", "-s", help="Nome da skill")
    parser.add_argument("--all", "-a", action="store_true", help="Rodar todos")
    parser.add_argument("--verbose", "-v", action="store_true", help="Output detalhado")
    parser.add_argument("--assess", action="store_true", help="Incluir avaliacao qualitativa")
    args = parser.parse_args()
    
    if args.all:
        for project in find_projects():
            skills = find_skills(project)
            for skill in skills:
                result = test_skill(project, skill, args.verbose)
                if "error" in result:
                    print(f"❌ {skill}: {result['error']}")
                else:
                    print(f"\n🎯 {skill}: {result['summary']['avg_score']}/10 | {result['summary']['pass_rate']}")
                    if args.verbose:
                        for platform, data in result["platforms"].items():
                            print(f"  {platform}: {data['avg_score']}/10")
    
    elif args.project and args.skill:
        if args.assess:
            result = assess_quality(args.project, args.skill, args.verbose)
            print_full_report(result, args.skill)
        else:
            result = test_skill(args.project, args.skill, args.verbose)
            if "error" in result:
                print(f"❌ Erro: {result['error']}")
            else:
                print(f"\n🎯 {result['skill']}")
                print("=" * 50)
                for platform, data in result["platforms"].items():
                    print(f"\n🔵 {platform.upper()}")
                    print(f"   Score: {data['avg_score']}/10 | Pass: {data['pass_rate']}")
                    if args.verbose:
                        for r in data["results"]:
                            status = "✅" if r["passed"] else "❌"
                            print(f"   {status} Test {r['test_id']}: {r['score']}/10")
                            for issue in r.get("issues", []):
                                print(f"      ⚠️  {issue}")
                print(f"\n📊 TOTAL: {result['summary']['avg_score']}/10")
    
    elif args.skill:
        for project in find_projects():
            if args.skill in find_skills(project):
                result = test_skill(project, args.skill, args.verbose)
                if "error" not in result:
                    print(f"\n🎯 {result['skill']} ({project}): {result['summary']['avg_score']}/10")
                    break
    else:
        print("Usage:")
        print("  python test_skill.py --project lovel --skill hunting [--verbose] [--assess]")
        print("  python test_skill.py --skill hunting")
        print("  python test_skill.py --all")


# =============================================================================
# QUALITATIVE ASSESSMENT (Avaliacao qualitativa via LLM)
# =============================================================================

QUALITY_PROMPT = """Você é um evaluator especialista em prompts de recruiting tech.

Avalie o prompt abaixo em 5 contextos importantes para recruiting tech:

1. CLAREZA - As instruções são claras e objetivas?
2. EXEMPLOS - Os exemplos são bons e representativos?
3. TOM - O tom está adequado (humano, direto, não formal)?
4. ESTRUTURA - A estrutura está lógica e fácil de seguir?
5. COMPLETUDE - Tem todas as informações necessárias?

Retorne o resultado no formato JSON abaixo (sem outros texto):
{{"json}}
{{"scores": {{"clareza": "<1-10>", "exemplos": "<1-10>", "tom": "<1-10>", "estrutura": "<1-10>", "completude": "<1-10>"}}, "media": "<media>", "issues": ["issue"], "suggestions": ["sugestao"], "overall": "Excelente|Bom|Razoavel|Precisa melhorar"}}
{{"json"}}

---

PROMPT A EVALUAR:
{prompt}
"""


def find_skill_content(project: str, skill: str, platform: str | None = None) -> Optional[Dict[str, Any]]:
    """Encontra conteúdo de uma skill."""
    project_dir = ROOT / "projects" / project / "skills"
    
    platforms: List[str] = [platform] if platform else ["claude", "chatgpt"]
    
    for plat in platforms:
        skill_md = project_dir / plat / skill / "SKILL.md"
        if skill_md.exists():
            return {"platform": plat, "path": skill_md, "content": skill_md.read_text()}
        
        skill_file = project_dir / plat / f"skill_{skill}.md"
        if skill_file.exists():
            return {"platform": plat, "path": skill_file, "content": skill_file.read_text()}
    
    return None


def extract_scores(text: str) -> Dict[str, Any]:
    """Extrai scores do texto de resposta do LLM."""
    import json
    import re
    
    json_match = re.search(r'```json\s*(\{.*?\})\s*```', text, re.DOTALL)
    if json_match:
        try:
            return json.loads(json_match.group(1))
        except json.JSONDecodeError:
            pass
    
    json_match = re.search(r'\{[\s\S]*\}', text)
    if json_match:
        try:
            data = json.loads(json_match.group())
            if "scores" in data:
                return data
        except json.JSONDecodeError:
            pass
    
    return {}


def assess_quality(project: str, skill: str, verbose: bool = False) -> Dict[str, Any]:
    """Avalia qualidade qualitativa de uma skill via LLM."""
    result = {"deterministic": None, "qualitative": {}}
    
    # 1. DETERMINISTIC - ja feito em test_skill()
    det_result = test_skill(project, skill, False)
    result["deterministic"] = det_result
    
    # 2. QUALITATIVE - avaliar cada platform
    for plat in ["claude", "chatgpt"]:
        content = find_skill_content(project, skill, plat)
        if not content:
            continue
        
        prompt = QUALITY_PROMPT.format(prompt=content["content"])
        llm_resp = call_llm(prompt)
        
        scores = extract_scores(llm_resp.get("output", ""))
        result["qualitative"][plat] = {
            "scores": scores,
            "raw": llm_resp.get("output", "")[:500] if verbose else ""
        }
    
    return result


def print_full_report(result: Dict[str, Any], skill: str) -> None:
    """Imprime relatório completo."""
    print(f"\n{'='*60}")
    print(f"🎯 {skill.upper()}")
    print("=" * 60)
    
    # Deterministic results
    if result.get("deterministic"):
        det = result["deterministic"]
        if "error" not in det:
            print("\n📋 TESTE DETERMINISTICO (patterns)")
            print("-" * 40)
            for plat, data in det.get("platforms", {}).items():
                emoji = "✅" if data["avg_score"] >= 7 else "⚠️" if data["avg_score"] >= 5 else "❌"
                print(f"   {emoji} {plat.upper()}: {data['avg_score']}/10 ({data['pass_rate']})")
            
            total = det.get("summary", {}).get("avg_score", 0)
            print(f"\n   📊 MEDIA DETERMINISTICA: {total}/10")
    
    # Qualitative results
    if result.get("qualitative"):
        print("\n📋 AVALIACAO QUALITATIVA (LLM judge)")
        print("-" * 40)
        
        all_media = []
        for plat, data in result["qualitative"].items():
            scores = data.get("scores", {})
            media = scores.get("media", 0)
            overall = scores.get("overall", "N/A")
            all_media.append(media)
            
            print(f"\n   🔵 {plat.upper()}")
            print(f"   📈 Media: {media:.1f}/10 - {overall}")
            
            if scores.get("scores"):
                for criterion, score in scores["scores"].items():
                    if criterion not in ["media", "overall"]:
                        e = "✅" if score >= 7 else "⚠️" if score >= 5 else "❌"
                        print(f"      {e} {criterion}: {score}/10")
            
            if scores.get("issues"):
                print(f"   🔴 Issues:")
                for issue in scores["issues"][:3]:
                    print(f"      - {issue[:80]}")
            
            if scores.get("suggestions"):
                print(f"   💡 Sugestoes:")
                for sug in scores["suggestions"][:3]:
                    print(f"      - {sug[:80]}")
        
        if all_media:
            print(f"\n   📊 MEDIA QUALITATIVA: {sum(all_media)/len(all_media):.1f}/10")
    
    # Combined score
    if result.get("deterministic") and result.get("qualitative"):
        det_avg = result["deterministic"].get("summary", {}).get("avg_score", 0)
        qual_avg = sum(q.get("scores", {}).get("media", 0) for q in result["qualitative"].values()) / len(result["qualitative"])
        combined = (det_avg + qual_avg) / 2
        print(f"\n{'='*60}")
        print(f"📊 COMBINED SCORE: {combined:.1f}/10")
        print(f"   (Deterministic: {det_avg:.1f} + Qualitative: {qual_avg:.1f}) / 2")
        print("=" * 60)


def main_assess():
    """Main para avaliacao qualitativa."""
    import argparse
    parser = argparse.ArgumentParser(description="Skill Quality Assessor")
    parser.add_argument("--project", "-p", default="lovel", help="Nome do projeto")
    parser.add_argument("--skill", "-s", help="Nome da skill")
    parser.add_argument("--all", "-a", action="store_true", help="Todas as skills")
    parser.add_argument("--verbose", "-v", action="store_true", help="Output completo")
    args = parser.parse_args()
    
    if args.all:
        for skill in ["hunting", "outreach", "post", "parecer"]:
            result = assess_quality(args.project, skill, args.verbose)
            print_full_report(result, skill)
    elif args.skill:
        result = assess_quality(args.project, args.skill, args.verbose)
        print_full_report(result, args.skill)
    else:
        print("Usage:")
        print("  python test_skill.py --skill hunting --assess")
        print("  python test_skill.py --all --assess")


if __name__ == "__main__":
    if "--assess" in sys.argv:
        sys.argv = [a for a in sys.argv if a != "--assess"]
        main_assess()
    else:
        main()
