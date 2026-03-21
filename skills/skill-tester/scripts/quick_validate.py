#!/usr/bin/env python3
"""
Quick Validate - Validação rápida de estrutura de skills.

Este script é agnóstico - funciona para qualquer projeto.

Usage:
    python scripts/quick_validate.py                           # Valida todas as skills
    python scripts/quick_validate.py --project lovel           # Valida projeto específico
    python scripts/quick_validate.py --project lovel --skill hunting
"""

import sys
import re
from pathlib import Path
from typing import List, Dict, Any

SKILLS_ROOT = Path(__file__).parent.parent.parent.parent

def validate_skill_structure(skill_path: Path) -> dict:
    """Valida estrutura básica de uma skill"""
    errors = []
    warnings = []
    
    # Check if it's a file or directory
    if skill_path.is_file():
        skill_md = skill_path
    else:
        # Try SKILL.md (claude format) or skill_{name}.md (chatgpt format)
        skill_md = skill_path / "SKILL.md"
        if not skill_md.exists():
            skill_name = skill_path.name
            skill_md = skill_path.parent / f"skill_{skill_name}.md"
    
    if not skill_md.exists():
        errors.append(f"Skill file not found: {skill_md}")
        return {"valid": False, "errors": errors, "warnings": warnings}
    
    content = skill_md.read_text()
    
    # YAML format
    if content.startswith("---"):
        if "name:" not in content:
            errors.append("Falta campo 'name' no frontmatter")
        if "description:" not in content:
            errors.append("Falta campo 'description' no frontmatter")
        
        if "Use para:" not in content:
            warnings.append("Sugestão: Adicionar 'Use para:'")
        if "Não use para:" not in content:
            warnings.append("Sugestão: Adicionar 'Não use para:'")
        
        desc_match = re.search(r'description:\s*"([^"]+)"', content)
        if desc_match:
            desc_len = len(desc_match.group(1))
            if desc_len < 50:
                warnings.append(f"Sugestão: Description muito curta ({desc_len} chars)")
    else:
        # XML format
        if "<skill" not in content:
            errors.append("Falta tag <skill>")
    
    has_evals = False
    if skill_path.is_dir():
        evals_dir = skill_path / "evals"
        if evals_dir.exists():
            evals_file = evals_dir / "testes.cue"
            if evals_file.exists():
                has_evals = True
            else:
                warnings.append("Diretório evals sem testes.cue")
    
    return {"valid": len(errors) == 0, "errors": errors, "warnings": warnings, "has_evals": has_evals}


def find_all_skills() -> List[Dict[str, Any]]:
    """Encontra todas as skills em todos os projetos."""
    skills = []
    projects_dir = SKILLS_ROOT / "projects"
    
    if not projects_dir.exists():
        return skills
    
    for project in projects_dir.iterdir():
        if not project.is_dir():
            continue
        
        skills_dir = project / "skills"
        if not skills_dir.exists():
            continue
        
        for platform in ["claude", "chatgpt"]:
            platform_dir = skills_dir / platform
            if not platform_dir.exists():
                continue
            
            for skill_dir in platform_dir.iterdir():
                if not skill_dir.is_dir() or skill_dir.name.startswith("."):
                    continue
                
                skills.append({
                    "project": project.name,
                    "platform": platform,
                    "name": skill_dir.name,
                    "path": skill_dir
                })
    
    return skills


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Quick Validate - Skill structure validator")
    parser.add_argument("--project", "-p", help="Filtrar por projeto")
    parser.add_argument("--platform", help="Filtrar por plataforma (claude, chatgpt)")
    args = parser.parse_args()
    
    print("🔍 Quick Validate")
    print("=" * 50)
    
    skills = find_all_skills()
    
    if not skills:
        print("Nenhuma skill encontrada em projects/")
        sys.exit(1)
    
    all_valid = True
    
    # Group by project
    projects = {}
    for skill in skills:
        key = skill["project"]
        if key not in projects:
            projects[key] = []
        projects[key].append(skill)
    
    for project, project_skills in projects.items():
        if args.project and project != args.project:
            continue
        
        print(f"\n🔵 Projeto: {project.upper()}")
        print("-" * 30)
        
        for skill in project_skills:
            if args.platform and skill["platform"] != args.platform:
                continue
            
            print(f"   📁 {skill['platform']}/{skill['name']}...", end=" ")
            result = validate_skill_structure(skill["path"])
            
            if result.get("has_evals"):
                print("📋", end=" ")
            
            if result["valid"]:
                print("✅")
            else:
                print("❌")
                for error in result["errors"]:
                    print(f"      ❌ {error}")
                all_valid = False
            
            for warning in result["warnings"]:
                print(f"      ⚠️  {warning}")
    
    print("\n" + "=" * 50)
    if all_valid:
        print("✅ Todas as skills são válidas!")
    else:
        print("❌ Algumas skills têm erros")


if __name__ == "__main__":
    main()
