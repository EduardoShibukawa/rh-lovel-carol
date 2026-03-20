#!/usr/bin/env python3
"""
Assess Quality - Validação subjetiva de skills via LLM.

Avalia qualidade de prompts de forma subjetiva:
- Clareza das instruções
- Qualidade dos exemplos
- Tom adequado
- Estrutura lógica
- Completude

Usage:
    python scripts/assess.py --project lovel --skill hunting
    python scripts/assess.py --project lovel
    python scripts/assess.py --skill hunting
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Any

import llm_client

ROOT = Path(__file__).resolve().parent.parent.parent.parent


QUALITY_PROMPT = """Você é um evaluator especialista em prompts de recruiting tech.

Avalie o prompt abaixo em {n_contextos} contextos importantes para recruiting tech:

1. CLAREZA - As instruções são claras e objetivas?
2. EXEMPLOS - Os exemplos são bons e representativos?
3. TOM - O tom está adequado (humano, direto, não formal)?
4. ESTRUTURA - A estrutura está lógica e fácil de seguir?
5. COMPLETUDE - Tem todas as informações necessárias?

Retorne o resultado no formato JSON abaixo (sem outros texto):
```json
{{
    "scores": {{
        "clareza": <1-10>,
        "exemplos": <1-10>,
        "tom": <1-10>,
        "estrutura": <1-10>,
        "completude": <1-10>
    }},
    "media": <media dos scores>,
    "issues": [
        "Problema específico encontrado (se houver)"
    ],
    "suggestions": [
        "Sugestão de melhoria (se houver)"
    ],
    "overall": "Excelente|Bom|Razoável|Precisa melhorar"
}}
```

---

PROMPT A EVALUAR:
{prompt}
"""


def find_skill_content(project: str, skill: str) -> Dict[str, Any]:
    """Encontra conteúdo de uma skill."""
    project_dir = ROOT / "projects" / project / "skills"
    
    for platform in ["claude", "chatgpt"]:
        skill_md = project_dir / platform / skill / "SKILL.md"
        if skill_md.exists():
            return {
                "platform": platform,
                "path": skill_md,
                "content": skill_md.read_text()
            }
        
        skill_file = project_dir / platform / f"skill_{skill}.md"
        if skill_file.exists():
            return {
                "platform": platform,
                "path": skill_file,
                "content": skill_file.read_text()
            }
    
    return None


def assess_skill(project: str, skill: str) -> Dict[str, Any]:
    """Avalia qualidade de uma skill via LLM."""
    result = find_skill_content(project, skill)
    
    if not result:
        return {"error": f"Skill '{skill}' não encontrada em projects/{project}/"}
    
    prompt = QUALITY_PROMPT.format(
        n_contextos=5,
        prompt=result["content"]
    )
    
    llm_response = llm_client.call_llm(prompt)
    
    if llm_response.get("error"):
        return {"error": llm_response["error"]}
    
    return {
        "skill": skill,
        "platform": result["platform"],
        "scores": extract_scores(llm_response["output"]),
        "raw_response": llm_response["output"]
    }


def extract_scores(text: str) -> Dict[str, Any]:
    """Extrai scores do texto de resposta do LLM."""
    import json
    import re
    
    # Tentar extrair JSON do bloco de código
    json_match = re.search(r'```json\s*(\{.*?\})\s*```', text, re.DOTALL)
    if json_match:
        try:
            data = json.loads(json_match.group(1))
            return data
        except json.JSONDecodeError:
            pass
    
    # Tentar extrair qualquer JSON válido
    json_match = re.search(r'\{[\s\S]*\}', text)
    if json_match:
        try:
            data = json.loads(json_match.group())
            if "scores" in data:
                return data
        except json.JSONDecodeError:
            pass
    
    # Fallback: extrair manualmente
    scores = {}
    for criterion in ["clareza", "exemplos", "tom", "estrutura", "completude"]:
        match = re.search(rf'{criterion}["\s:]+(\d+)', text, re.IGNORECASE)
        if match:
            scores[criterion] = int(match.group(1))
    
    return scores


def print_assessment(result: Dict[str, Any]) -> None:
    """Imprime resultado da avaliação."""
    if "error" in result:
        print(f"   ❌ Erro: {result['error']}")
        return
    
    scores = result.get("scores", {})
    media = scores.get("media", 0)
    overall = scores.get("overall", "Desconhecido")
    
    print(f"   📊 {result['skill']} ({result['platform']})")
    
    if scores.get("scores"):
        for criterion, score in scores["scores"].items():
            if criterion != "media" and criterion != "overall":
                emoji = "✅" if score >= 7 else "⚠️" if score >= 5 else "❌"
                print(f"      {emoji} {criterion.capitalize()}: {score}/10")
    
    print(f"   📈 Média: {media:.1f}/10 - {overall}")
    
    if scores.get("issues"):
        print(f"   🔴 Issues:")
        for issue in scores["issues"]:
            print(f"      - {issue}")
    
    if scores.get("suggestions"):
        print(f"   💡 Sugestões:")
        for suggestion in scores["suggestions"]:
            print(f"      - {suggestion}")


def main():
    parser = argparse.ArgumentParser(description="Assess Quality - Skill quality evaluator")
    parser.add_argument("--project", "-p", help="Nome do projeto")
    parser.add_argument("--skill", "-s", help="Nome da skill específica")
    parser.add_argument("--all", "-a", action="store_true", help="Avaliar todos")
    
    args = parser.parse_args()
    
    llm_client.configure(llm_eval="opencode", llm_grading="opencode")
    
    # Encontrar projetos
    projects_dir = ROOT / "projects"
    if not projects_dir.exists():
        print("Nenhum projeto encontrado em projects/")
        sys.exit(1)
    
    projects = [p.name for p in projects_dir.iterdir() if p.is_dir()]
    
    if args.all:
        for project in projects:
            print(f"\n🎯 PROJECT: {project}")
            print("=" * 50)
            
            project_dir = projects_dir / project / "skills"
            for platform in ["claude", "chatgpt"]:
                platform_dir = project_dir / platform
                if not platform_dir.exists():
                    continue
                
                for skill_dir in platform_dir.iterdir():
                    if not skill_dir.is_dir() or skill_dir.name.startswith("."):
                        continue
                    
                    result = assess_skill(project, skill_dir.name)
                    print_assessment(result)
    
    elif args.project:
        if not args.skill:
            # Avaliar todas as skills do projeto
            project_dir = projects_dir / args.project / "skills"
            if not project_dir.exists():
                print(f"Projeto '{args.project}' não encontrado")
                sys.exit(1)
            
            print(f"\n🎯 PROJECT: {args.project}")
            print("=" * 50)
            
            for platform in ["claude", "chatgpt"]:
                platform_dir = project_dir / platform
                if not platform_dir.exists():
                    continue
                
                for skill_dir in platform_dir.iterdir():
                    if not skill_dir.is_dir() or skill_dir.name.startswith("."):
                        continue
                    
                    print(f"\n📋 Platform: {platform}")
                    result = assess_skill(args.project, skill_dir.name)
                    print_assessment(result)
        else:
            result = assess_skill(args.project, args.skill)
            print_assessment(result)
    
    elif args.skill:
        for project in projects:
            project_dir = projects_dir / project / "skills"
            for platform in ["claude", "chatgpt"]:
                skill_path = project_dir / platform / args.skill / "SKILL.md"
                if skill_path.exists():
                    print(f"\n🎯 SKILL: {args.skill} (em {project}/{platform})")
                    print("=" * 50)
                    result = assess_skill(project, args.skill)
                    print_assessment(result)
                    sys.exit(0)
        
        print(f"Skill '{args.skill}' não encontrada")
        sys.exit(1)
    
    else:
        print("Usage:")
        print("  python assess.py --project lovel --skill hunting")
        print("  python assess.py --project lovel")
        print("  python assess.py --skill hunting")
        print("  python assess.py --all")
        sys.exit(1)


if __name__ == "__main__":
    main()
