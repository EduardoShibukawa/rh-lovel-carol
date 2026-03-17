#!/usr/bin/env python3
"""
Lovel Quick Validate - Validação rápida de skills
Baseado em quick_validate.py da skill-creator (Anthropic)

Usage:
    python scripts/quick_validate.py                    # Valida todas
    python scripts/quick_validate.py hunting            # Valida apenas hunting
    python scripts/quick_validate.py claude/hunting     # Valida skill específica
    python scripts/quick_validate.py chatgpt             # Valida plataforma específica
"""

import json
import sys
import re
from pathlib import Path

SKILLS_ROOT = Path(__file__).parent.parent

def validate_skill_structure(skill_path: Path) -> dict:
    """Valida estrutura básica de uma skill"""
    errors = []
    warnings = []
    
    # Check if it's a file or directory
    if skill_path.is_file():
        skill_md = skill_path
    else:
        skill_md = skill_path / "SKILL.md"
    
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
    
    if skill_path.is_dir():
        evals_dir = skill_path / "evals"
        if evals_dir.exists():
            evals_file = evals_dir / "evals.json"
            if evals_file.exists():
                print(f"         📋 Evals found")
            else:
                warnings.append("Diretório evals sem evals.json")
    
    return {"valid": len(errors) == 0, "errors": errors, "warnings": warnings}

def main():
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    
    print("🔍 Lovel Quick Validate")
    print("=" * 50)
    
    if not args:
        # Validate all
        platforms = {
            "claude": {"base": "prompts/web/claude", "skills": ["hunting", "outreach", "post", "parecer", "skill"]},
            "chatgpt": {"base": "prompts/web/chatgpt/skills", "skills": ["skill_hunting.md", "skill_outreach.md", "skill_post.md", "skill_parecer.md"]},
            "root": {"base": ".", "skills": ["tester"]}
        }
        
        all_valid = True
        for platform, config in platforms.items():
            print(f"\n🔵 Plataforma: {platform.upper()}")
            print("-" * 30)
            
            base = SKILLS_ROOT / config["base"]
            for skill in config["skills"]:
                skill_path = base / skill
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
    else:
        # Validate specific skill
        target = args[0]
        
        # Try different paths
        paths_to_try = [
            SKILLS_ROOT / target,
            SKILLS_ROOT / "prompts/web/claude" / target,
            SKILLS_ROOT / "prompts/web/chatgpt/skills" / target,
            SKILLS_ROOT / "prompts/web/claude" / target / "SKILL.md",
            SKILLS_ROOT / "prompts/web/chatgpt/skills" / target,
        ]
        
        found = False
        for path in paths_to_try:
            if path.exists():
                found = True
                print(f"\n📁 Validando: {path}")
                result = validate_skill_structure(path)
                
                if result["valid"]:
                    print(f"   ✅ Válido")
                else:
                    print(f"   ❌ Inválido")
                    for error in result["errors"]:
                        print(f"      - {error}")
                
                for warning in result["warnings"]:
                    print(f"   ⚠️  {warning}")
                break
        
        if not found:
            print(f"❌ Skill não encontrada: {target}")
            print("\nUsage:")
            print("  python scripts/quick_validate.py              # Todas")
            print("  python scripts/quick_validate.py hunting      # Apenas hunting")
            print("  python scripts/quick_validate.py claude/hunting")

if __name__ == "__main__":
    main()
