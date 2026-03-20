#!/usr/bin/env python3
"""
Validate - Validação determinística de fixtures CUE.

Valida que os fixtures de teste estão corretos usando CUE.

Usage:
    python validate.py --project lovel --skill hunting
    python validate.py --project lovel
    python validate.py --skill hunting
    python validate.py --all
"""

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Any

ROOT = Path(__file__).resolve().parent.parent.parent.parent


def find_fixtures(project: str, skill: str) -> Path:
    """Encontra fixtures CUE para projeto/skill."""
    project_dir = ROOT / "projects" / project / "skills"
    
    for platform in ["claude", "chatgpt"]:
        fixtures_file = project_dir / platform / skill / "evals" / "testes.cue"
        if fixtures_file.exists():
            return fixtures_file
    
    return None


def validate_with_cue(fixtures_file: Path) -> Dict[str, Any]:
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
                "issues": parse_cue_errors(result.stderr)
            }
    
    except FileNotFoundError:
        return {"valid": False, "issues": ["CUE não encontrado - instale em cuelang.org"]}
    except subprocess.TimeoutExpired:
        return {"valid": False, "issues": ["Timeout na validação"]}
    except Exception as e:
        return {"valid": False, "issues": [str(e)]}


def parse_cue_errors(stderr: str) -> List[str]:
    """Parse erros do CUE para formato legível."""
    lines = stderr.strip().split("\n")
    errors = []
    
    for line in lines:
        if line.strip():
            # Simplificar mensagens de erro
            if ":" in line:
                parts = line.split(":", 1)
                errors.append(parts[-1].strip())
            else:
                errors.append(line.strip())
    
    return errors[:5]  # Limitar a 5 erros


def validate_skill(project: str, skill: str) -> Dict[str, Any]:
    """Valida uma skill específica."""
    fixtures_file = find_fixtures(project, skill)
    
    if not fixtures_file:
        return {"valid": False, "issues": ["Fixtures não encontrados"]}
    
    result = validate_with_cue(fixtures_file)
    result["skill"] = skill
    result["fixtures"] = str(fixtures_file)
    
    return result


def print_validation(result: Dict[str, Any]) -> None:
    """Imprime resultado da validação."""
    if result.get("valid"):
        print(f"   ✅ {result['skill']}: Fixtures válidos")
    else:
        print(f"   ❌ {result['skill']}: Fixtures inválidos")
        for issue in result.get("issues", []):
            print(f"      - {issue}")


def main():
    parser = argparse.ArgumentParser(description="Validate - CUE fixtures validator")
    parser.add_argument("--project", "-p", help="Nome do projeto")
    parser.add_argument("--skill", "-s", help="Nome da skill específica")
    parser.add_argument("--all", "-a", action="store_true", help="Validar todos")
    
    args = parser.parse_args()
    
    projects_dir = ROOT / "projects"
    if not projects_dir.exists():
        print("Nenhum projeto encontrado em projects/")
        sys.exit(1)
    
    projects = [p.name for p in projects_dir.iterdir() if p.is_dir()]
    
    if args.all:
        all_results = []
        
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
                    
                    result = validate_skill(project, skill_dir.name)
                    print_validation(result)
                    all_results.append(result)
        
        # Summary
        valid = sum(1 for r in all_results if r.get("valid"))
        total = len(all_results)
        print(f"\n📊 TOTAL: {valid}/{total} válidos ({(valid/total*100) if total else 0:.0f}%)")
    
    elif args.project:
        project_dir = projects_dir / args.project / "skills"
        
        if not project_dir.exists():
            print(f"Projeto '{args.project}' não encontrado")
            sys.exit(1)
        
        print(f"\n🎯 PROJECT: {args.project}")
        print("=" * 50)
        
        if args.skill:
            result = validate_skill(args.project, args.skill)
            print_validation(result)
        else:
            all_results = []
            
            for platform in ["claude", "chatgpt"]:
                platform_dir = project_dir / platform
                if not platform_dir.exists():
                    continue
                
                print(f"\n🔵 Platform: {platform}")
                
                for skill_dir in platform_dir.iterdir():
                    if not skill_dir.is_dir() or skill_dir.name.startswith("."):
                        continue
                    
                    result = validate_skill(args.project, skill_dir.name)
                    print_validation(result)
                    all_results.append(result)
            
            valid = sum(1 for r in all_results if r.get("valid"))
            total = len(all_results)
            print(f"\n📊 PROJECT: {valid}/{total} válidos")
    
    elif args.skill:
        found = False
        
        for project in projects:
            project_dir = projects_dir / project / "skills"
            for platform in ["claude", "chatgpt"]:
                fixtures = find_fixtures(project, args.skill)
                if fixtures:
                    print(f"\n🎯 SKILL: {args.skill} (em {project}/{platform})")
                    print("=" * 50)
                    result = validate_skill(project, args.skill)
                    print_validation(result)
                    found = True
                    break
        
        if not found:
            print(f"Skill '{args.skill}' não encontrada")
            sys.exit(1)
    
    else:
        print("Usage:")
        print("  python validate.py --project lovel --skill hunting")
        print("  python validate.py --project lovel")
        print("  python validate.py --skill hunting")
        print("  python validate.py --all")
        sys.exit(1)


if __name__ == "__main__":
    main()
