#!/usr/bin/env python3
"""
Lovel Improve Description - Otimiza description para triggering
Baseado em improve_description.py da skill-creator (Anthropic)
"""

import json
import sys
import re
from pathlib import Path

def improve_description(skill_path: str) -> dict:
    """Melhora description de uma skill para melhor triggering"""
    
    skill_md = Path(skill_path) / "SKILL.md"
    if not skill_md.exists():
        return {"error": "SKILL.md não encontrado"}
    
    content = skill_md.read_text()
    
    # Extract current description
    desc_match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not desc_match:
        return {"error": "Frontmatter não encontrado"}
    
    frontmatter = desc_match.group(1)
    
    # Check if description is too short
    if "description:" in frontmatter:
        desc_line = [l for l in frontmatter.split('\n') if l.startswith('description:')][0]
        desc_len = len(desc_line)
        
        if desc_len < 100:
            print(f"⚠️  Description muito curta ({desc_len} chars)")
            print("   Sugestão: Adicione mais contextos de uso")
    
    # Check if lacks "Use for" or "Don't use for"
    if "Use para:" not in content:
        print("⚠️  Falta 'Use para:' - ajuda triggering")
    
    if "Não use para:" not in content:
        print("⚠️  Falta 'Não use para:' - ajuda triggering")
    
    return {
        "suggestions": [
            "Tornar description mais 'pushy' para evitar undertriggering",
            "Adicionar contextos específicos de quando usar",
            "Adicionar 'Não use para' para evitar falsos positivos"
        ]
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python improve_description.py <skill-path>")
        sys.exit(1)
    
    skill_path = sys.argv[1]
    result = improve_description(skill_path)
    
    if "error" in result:
        print(f"❌ {result['error']}")
    else:
        print("✅ Análise concluída")
        for suggestion in result.get("suggestions", []):
            print(f"   💡 {suggestion}")

if __name__ == "__main__":
    main()
