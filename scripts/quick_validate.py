#!/usr/bin/env python3
"""
Lovel Quick Validate - Validação rápida de skills
Baseado em quick_validate.py da skill-creator (Anthropic)
"""

import json
import sys
from pathlib import Path

SKILLS_PATH = Path(__file__).parent.parent

def validate_skill_structure(skill_path: Path) -> dict:
    """Valida estrutura básica de uma skill"""
    errors = []
    warnings = []
    
    # Check if it's a file or directory
    if skill_path.is_file():
        # ChatGPT format: single .md file
        skill_md = skill_path
    else:
        # Claude format: directory with SKILL.md
        skill_md = skill_path / "SKILL.md"
    
    if not skill_md.exists():
        errors.append(f"Skill file not found: {skill_md}")
        return {"valid": False, "errors": errors, "warnings": warnings}
    
    # Check YAML frontmatter
    content = skill_md.read_text()
    
    # For Claude skills (YAML format)
    if content.startswith("---"):
        if "name:" not in content:
            errors.append("Falta campo 'name' no frontmatter")
        if "description:" not in content:
            errors.append("Falta campo 'description' no frontmatter")
        
        # Check for improvements
        if "Use para:" not in content:
            warnings.append("Sugestão: Adicionar 'Use para:'")
        if "Não use para:" not in content:
            warnings.append("Sugestão: Adicionar 'Não use para:'")
        
        # Check description length
        import re
        desc_match = re.search(r'description:\s*"([^"]+)"', content)
        if desc_match:
            desc_len = len(desc_match.group(1))
            if desc_len < 50:
                warnings.append(f"Sugestão: Description muito curta ({desc_len} chars), considere adicionar mais contextos")
    else:
        # ChatGPT format (XML)
        if "<skill" not in content:
            errors.append("Falta tag <skill> no arquivo")
    
    # Check evals directory (Claude only)
    if skill_path.is_dir():
        evals_dir = skill_path / "evals"
        if evals_dir.exists():
            evals_file = evals_dir / "evals.json"
            if evals_file.exists():
                print(f"         📋 Evals found")
            else:
                warnings.append("Diretório evals sem evals.json")
    
    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings
    }

def main():
    print("🔍 Lovel Quick Validate")
    print("=" * 50)
    
    # Check both Claude and ChatGPT skills
    platforms = {
        "claude": {
            "base": "prompts/web/claude",
            "skills": ["hunting", "outreach", "post", "parecer"]
        },
        "chatgpt": {
            "base": "prompts/web/chatgpt/skills",
            "skills": ["skill_hunting.md", "skill_outreach.md", "skill_post.md"]
        }
    }
    
    all_valid = True
    
    for platform, config in platforms.items():
        print(f"\n🔵 Plataforma: {platform.upper()}")
        print("-" * 30)
        
        base_path = SKILLS_PATH / config["base"]
        
        for skill in config["skills"]:
            skill_path = base_path / skill
            
            if not skill_path.exists():
                print(f"   ⚠️  {skill}: não encontrado")
                continue
            
            print(f"   📁 Validando {skill}...")
            result = validate_skill_structure(skill_path)
            
            if result["valid"]:
                print(f"      ✅ Válido")
            else:
                print(f"      ❌ Inválido")
                for error in result["errors"]:
                    print(f"         - {error}")
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
