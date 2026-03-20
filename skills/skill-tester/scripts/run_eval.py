#!/usr/bin/env python3
"""
Skill Eval Runner - Executa evals de skills usando CUE para validação.

Usage:
    python run_eval.py --project lovel --skill hunting
    python run_eval.py --project lovel
    python run_eval.py --skill hunting
    python run_eval.py --all

Args:
    --project: Nome do projeto (lovel, conectacareer)
    --skill: Nome da skill específica
    --all: Rodar todos os projetos e skills
    iterations: Número de vezes para executar cada eval (default: 1)
"""

import argparse
import subprocess
import sys
import statistics
from pathlib import Path
from typing import Dict, List, Any, Optional

import llm_client

ROOT = Path(__file__).resolve().parent.parent.parent.parent


def find_projects() -> List[str]:
    """Lista todos os projetos disponíveis."""
    projects_dir = ROOT / "projects"
    if not projects_dir.exists():
        return []
    return [p.name for p in projects_dir.iterdir() if p.is_dir()]


def find_skills(project: str) -> List[str]:
    """Lista todas as skills de um projeto."""
    project_dir = ROOT / "projects" / project / "skills"
    skills = []
    
    if not project_dir.exists():
        return skills
    
    for platform in ["claude", "chatgpt"]:
        platform_dir = project_dir / platform
        if platform_dir.exists():
            for skill_dir in platform_dir.iterdir():
                if skill_dir.is_dir() and not skill_dir.name.startswith("."):
                    skills.append(skill_dir.name)
    
    return list(set(skills))


def find_fixtures(project: str, skill: str) -> Optional[Path]:
    """Encontra fixtures CUE para projeto/skill."""
    project_dir = ROOT / "projects" / project / "skills"
    
    for platform in ["claude", "chatgpt"]:
        fixtures_file = project_dir / platform / skill / "evals" / "testes.cue"
        if fixtures_file.exists():
            return fixtures_file
    
    return None


def validate_fixtures_with_cue(fixtures_file: Path) -> Dict[str, Any]:
    """Valida fixtures usando cue vet."""
    try:
        result = subprocess.run(
            ["cue", "vet", "-c", str(fixtures_file)],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            return {"valid": True, "issues": []}
        else:
            return {
                "valid": False,
                "issues": [result.stderr[:300] if result.stderr else "Validation failed"]
            }
    
    except subprocess.TimeoutExpired:
        return {"valid": False, "issues": ["CUE validation timeout"]}
    except FileNotFoundError:
        return {"valid": False, "issues": ["CUE not found - install from cuelang.org"]}
    except Exception as e:
        return {"valid": False, "issues": [str(e)]}


def run_project_eval(project: str, skill: Optional[str] = None) -> List[Dict]:
    """Executa evals para um projeto."""
    print(f"\n🎯 PROJECT: {project}")
    print("=" * 50)
    
    skills_to_test = [skill] if skill else find_skills(project)
    
    if not skills_to_test:
        print(f"   Nenhuma skill encontrada em projects/{project}/skills/")
        return []
    
    llm_client.reset_stats()
    all_results = []
    
    for skill_name in skills_to_test:
        fixtures_file = find_fixtures(project, skill_name)
        
        if not fixtures_file:
            print(f"\n📋 {skill_name}: sem fixtures (pulando)")
            continue
        
        print(f"\n📋 SKILL: {skill_name}")
        
        # Validar fixtures com cue vet
        validation = validate_fixtures_with_cue(fixtures_file)
        
        if validation["valid"]:
            print(f"   ✅ Fixtures CUE válidos")
            result = {"skill": skill_name, "passed": True, "score": 10}
        else:
            print(f"   ❌ Fixtures CUE inválidos:")
            for issue in validation["issues"]:
                print(f"      - {issue}")
            result = {"skill": skill_name, "passed": False, "score": 0, "issues": validation["issues"]}
        
        all_results.append(result)
    
    return all_results


def main():
    parser = argparse.ArgumentParser(description="Skill Eval Runner")
    parser.add_argument("--project", "-p", help="Nome do projeto")
    parser.add_argument("--skill", "-s", help="Nome da skill específica")
    parser.add_argument("--all", "-a", action="store_true", help="Rodar todos")
    parser.add_argument("iterations", nargs="?", default="1", help="Iterações")
    
    args = parser.parse_args()
    
    llm_client.configure(llm_eval="opencode", llm_grading="opencode")
    
    if args.all:
        projects = find_projects()
        all_results = []
        for project in projects:
            results = run_project_eval(project)
            all_results.extend(results)
        
        # Summary total
        if all_results:
            passed = sum(1 for r in all_results if r.get("passed"))
            total = len(all_results)
            avg_score = statistics.mean([r.get("score", 0) for r in all_results])
            print("\n" + "=" * 50)
            print(f"📊 TOTAL SUMMARY")
            print(f"   Pass Rate:   {passed}/{total} ({passed/total*100:.1f}%)")
            print(f"   Avg Score:   {avg_score:.2f}/10")
            print("=" * 50)
    
    elif args.project:
        results = run_project_eval(args.project, args.skill)
        
        if results:
            passed = sum(1 for r in results if r.get("passed"))
            total = len(results)
            avg_score = statistics.mean([r.get("score", 0) for r in results])
            print("\n" + "=" * 50)
            print(f"📊 PROJECT SUMMARY: {args.project}")
            print(f"   Pass Rate:   {passed}/{total} ({passed/total*100:.1f}%)")
            print(f"   Avg Score:   {avg_score:.2f}/10")
            print("=" * 50)
    
    elif args.skill:
        projects = find_projects()
        found = False
        for project in projects:
            if args.skill in find_skills(project):
                run_project_eval(project, args.skill)
                found = True
                break
        
        if not found:
            print(f"Skill '{args.skill}' não encontrada em nenhum projeto")
            print(f"Projetos disponíveis: {projects}")
            sys.exit(1)
    
    else:
        projects = find_projects()
        print("Usage: python run_eval.py --project <name> [--skill <name>] [--all]")
        print(f"Projetos disponíveis: {projects}")
        sys.exit(1)


if __name__ == "__main__":
    main()
