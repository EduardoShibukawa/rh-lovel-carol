#!/usr/bin/env python3
"""
Test - Roda testes determinísticos e subjetivos de uma skill.

Usage:
    python scripts/test.py --project lovel --skill hunting
    python scripts/test.py --project lovel
    python scripts/test.py --all
"""

import argparse
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent.parent

sys.path.insert(0, str(Path(__file__).resolve().parent))
import llm_client

QUALITY_PROMPT = """Você é um evaluator especialista em prompts de recruiting tech.

Avalie o prompt abaixo em 5 contextos:

1. CLAREZA - Instruções claras e objetivas?
2. EXEMPLOS - Bons e representativos?
3. TOM - Humano, direto, não formal?
4. ESTRUTURA - Lógica e fácil de seguir?
5. COMPLETUDE - Todas informações necessárias?

Retorne JSON:
```json
{{
    "scores": {{
        "clareza": <1-10>,
        "exemplos": <1-10>,
        "tom": <1-10>,
        "estrutura": <1-10>,
        "completude": <1-10>
    }},
    "media": <0-10>,
    "issues": ["problema (se houver)"],
    "suggestions": ["sugestão (se houver)"],
    "overall": "Excelente|Bom|Razoável|Precisa melhorar"
}}
```

---

PROMPT AVALIADO:
{prompt}"""


def find_skill_content(project: str, skill: str) -> dict:
    """Encontra conteúdo de uma skill."""
    project_dir = ROOT / "projects" / project / "skills"
    
    for platform in ["claude", "chatgpt"]:
        skill_md = project_dir / platform / skill / "SKILL.md"
        if skill_md.exists():
            return {"platform": platform, "content": skill_md.read_text()}
        
        skill_file = project_dir / platform / f"skill_{skill}.md"
        if skill_file.exists():
            return {"platform": platform, "content": skill_file.read_text()}
    
    return None


def find_fixtures(project: str, skill: str) -> Path:
    """Encontra fixtures CUE."""
    project_dir = ROOT / "projects" / project / "skills"
    
    for platform in ["claude", "chatgpt"]:
        fixtures = project_dir / platform / skill / "evals" / "testes.cue"
        if fixtures.exists():
            return fixtures
    return None


def validate_cue(fixtures: Path) -> dict:
    """Valida fixtures com CUE."""
    try:
        result = subprocess.run(
            ["cue", "vet", "-c", str(fixtures)],
            capture_output=True,
            text=True,
            timeout=30
        )
        return {"valid": result.returncode == 0, "error": result.stderr if result.returncode else None}
    except FileNotFoundError:
        return {"valid": False, "error": "CUE não instalado"}
    except Exception as e:
        return {"valid": False, "error": str(e)}


def assess_llm(content: str) -> dict:
    """Avalia qualidade via LLM."""
    prompt = QUALITY_PROMPT.format(prompt=content)
    
    t0 = time.time()
    response = llm_client.call_llm(prompt)
    latency = time.time() - t0
    
    if response.get("error"):
        return {"error": response["error"]}
    
    # Parse JSON from response
    import json
    import re
    
    text = response.get("output", "")
    
    # Try to extract JSON
    json_match = re.search(r'```json\s*(\{.*?\})\s*```', text, re.DOTALL)
    if json_match:
        try:
            return {"data": json.loads(json_match.group(1)), "latency": latency}
        except json.JSONDecodeError:
            pass
    
    return {"error": "Não foi possível extrair scores", "raw": text[:200]}


def test_skill(project: str, skill: str) -> dict:
    """Testa uma skill (determinístico + subjetivo)."""
    result = {
        "skill": skill,
        "deterministic": {"valid": None},
        "subjective": {"score": None}
    }
    
    # 1. Validate CUE fixtures
    fixtures = find_fixtures(project, skill)
    if fixtures:
        cue_result = validate_cue(fixtures)
        result["deterministic"] = {"valid": cue_result["valid"], "error": cue_result.get("error")}
    else:
        result["deterministic"] = {"valid": False, "error": "Fixtures não encontrados"}
    
    # 2. Assess quality via LLM
    skill_content = find_skill_content(project, skill)
    if skill_content:
        result["platform"] = skill_content["platform"]
        llm_result = assess_llm(skill_content["content"])
        if "data" in llm_result:
            result["subjective"] = {
                "score": llm_result["data"].get("media", 0),
                "overall": llm_result["data"].get("overall", "?"),
                "scores": llm_result["data"].get("scores", {}),
                "issues": llm_result["data"].get("issues", []),
                "suggestions": llm_result["data"].get("suggestions", []),
                "latency": llm_result.get("latency", 0)
            }
        else:
            result["subjective"] = {"error": llm_result.get("error")}
    else:
        result["subjective"] = {"error": "Skill não encontrada"}
    
    return result


def print_result(r: dict) -> None:
    """Imprime resultado do teste."""
    skill = r.get("skill", "?")
    platform = r.get("platform", "?")
    
    print(f"\n📋 {skill} ({platform})")
    print("-" * 40)
    
    # Deterministic
    det = r.get("deterministic", {})
    if det.get("valid"):
        print("   ✅ CUE: Válido")
    else:
        print(f"   ❌ CUE: {det.get('error', 'Inválido')[:50]}")
    
    # Subjective
    sub = r.get("subjective", {})
    if sub.get("score") is not None:
        score = sub["score"]
        overall = sub.get("overall", "?")
        emoji = "✅" if score >= 9.5 else "⚠️" if score >= 7 else "❌"
        print(f"   {emoji} LLM: {score:.1f}/10 ({overall})")
        
        if sub.get("scores"):
            for key, val in sub["scores"].items():
                if key not in ["media", "overall"]:
                    print(f"      - {key}: {val}/10")
        
        if sub.get("issues"):
            print(f"   🔴 Issues: {sub['issues'][0][:60]}...")
    elif sub.get("error"):
        print(f"   ⚠️  LLM: {sub['error']}")
    
    return r.get("deterministic", {}).get("valid") and sub.get("score", 0) >= 7


def main():
    parser = argparse.ArgumentParser(description="Test - Deterministic + Subjective validation")
    parser.add_argument("--project", "-p", help="Projeto")
    parser.add_argument("--skill", "-s", help="Skill específica")
    parser.add_argument("--all", "-a", action="store_true", help="Todas as skills")
    
    args = parser.parse_args()
    
    llm_client.configure(llm_eval="opencode", llm_grading="opencode")
    
    projects_dir = ROOT / "projects"
    if not projects_dir.exists():
        print("Nenhum projeto encontrado")
        sys.exit(1)
    
    projects = [p.name for p in projects_dir.iterdir() if p.is_dir()]
    
    print("=" * 60)
    print("🧪 TEST - Deterministic + Subjective")
    print("=" * 60)
    
    all_passed = []
    
    if args.all:
        for project in projects:
            print(f"\n🎯 PROJECT: {project}")
            project_dir = projects_dir / project / "skills"
            
            for platform in ["claude", "chatgpt"]:
                platform_dir = project_dir / platform
                if not platform_dir.exists():
                    continue
                
                for skill_dir in platform_dir.iterdir():
                    if not skill_dir.is_dir() or skill_dir.name.startswith("."):
                        continue
                    
                    r = test_skill(project, skill_dir.name)
                    passed = print_result(r)
                    all_passed.append(passed)
    
    elif args.project:
        project_dir = projects_dir / args.project / "skills"
        
        if args.skill:
            r = test_skill(args.project, args.skill)
            print_result(r)
        else:
            for platform in ["claude", "chatgpt"]:
                platform_dir = project_dir / platform
                if not platform_dir.exists():
                    continue
                
                for skill_dir in platform_dir.iterdir():
                    if not skill_dir.is_dir() or skill_dir.name.startswith("."):
                        continue
                    
                    r = test_skill(args.project, skill_dir.name)
                    passed = print_result(r)
                    all_passed.append(passed)
    
    else:
        print("Usage: python test.py --project <name> [--skill <skill>] [--all]")
        sys.exit(1)
    
    # Summary
    if all_passed:
        passed = sum(1 for p in all_passed if p)
        total = len(all_passed)
        print(f"\n{'=' * 60}")
        print(f"📊 SUMMARY: {passed}/{total} skills passing")
        print("=" * 60)


if __name__ == "__main__":
    main()
