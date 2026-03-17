#!/usr/bin/env python3
"""
Lovel Quick Validate - Validação rápida de skills
Baseado em quick_validate.py da skill-creator (Anthropic)
"""

import json
import sys
from pathlib import Path

SKILLS_PATH = Path(__file__).parent.parent.parent

def validate_skill_structure(skill_path: Path) -> dict:
    """Valida estrutura básica de uma skill"""
    errors = []
    warnings = []
    
    # Check SKILL.md exists
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        errors.append(f"SKILL.md não encontrado em {skill_path}")
        return {"valid": False, "errors": errors, "warnings": warnings}
    
    # Check YAML frontmatter
    content = skill_md.read_text()
    if not content.startswith("---"):
        errors.append("SKILL.md deve começar com YAML frontmatter (---)")
    
    # Check name field
    if "name:" not in content:
        errors.append("Falta campo 'name' no frontmatter")
    
    # Check description field
    if "description:" not in content:
        errors.append("Falta campo 'description' no frontmatter")
    
    # Check evals directory
    evals_dir = skill_path / "evals"
    if evals_dir.exists():
        evals_file = evals_dir / "evals.json"
        if evals_file.exists():
            print(f"   ✅ Evals found")
        else:
            warnings.append("Diretório evals sem evals.json")
    
    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings
    }

def main():
    print("🔍 Lovel Quick Validate")
    print("=" * 40)
    
    skills_to_check = [
        "hunting",
        "outreach", 
        "post",
        "parecer"
    ]
    
    all_valid = True
    
    for skill in skills_to_check:
        skill_path = SKILLS_PATH / skill
        print(f"\n📁 Validando {skill}...")
        
        if not skill_path.exists():
            print(f"   ❌ Skill não encontrada: {skill}")
            all_valid = False
            continue
        
        result = validate_skill_structure(skill_path)
        
        if result["valid"]:
            print(f"   ✅ Válido")
        else:
            print(f"   ❌ Inválido")
            for error in result["errors"]:
                print(f"      - {error}")
            all_valid = False
        
        for warning in result["warnings"]:
            print(f"   ⚠️  {warning}")
    
    print("\n" + "=" * 40)
    if all_valid:
        print("✅ Todas as skills são válidas!")
    else:
        print("❌ Algumas skills têm erros")

if __name__ == "__main__":
    main()
