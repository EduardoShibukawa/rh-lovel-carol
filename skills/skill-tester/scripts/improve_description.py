#!/usr/bin/env python3
"""
Lovel Improve Description - Otimiza description para triggering
Baseado em improve_description.py da skill-creator (Anthropic)

Usage:
    python scripts/improve_description.py prompts/web/claude/hunting
    python scripts/improve_description.py prompts/web/claude/outreach
"""

import json
import sys
import re
from pathlib import Path

SKILLS_ROOT = Path(__file__).parent.parent.parent.parent

def analyze_description(skill_path: str) -> dict:
    """Analisa e sugere melhorias na description"""
    
    # Handle both file and directory paths
    skill_path_obj = Path(skill_path)
    if skill_path_obj.is_file():
        skill_md = skill_path_obj
    else:
        skill_md = skill_path_obj / "SKILL.md"
    
    if not skill_md.exists():
        return {"error": f"SKILL.md não encontrado: {skill_md}"}
    
    content = skill_md.read_text()
    issues = []
    suggestions = []
    
    # Check format
    is_yaml = content.startswith("---")
    
    if is_yaml:
        # Claude format
        desc_match = re.search(r'description:\s*"([^"]+)"', content)
        if desc_match:
            desc = desc_match.group(1)
            desc_len = len(desc)
            
            print(f"\n📝 Description atual ({desc_len} chars):")
            print(f"   {desc[:100]}...")
            
            if desc_len < 50:
                issues.append(f"Description muito curta ({desc_len} chars)")
                suggestions.append("Adicione mais contextos de uso (mínimo 50 chars)")
            elif desc_len < 100:
                issues.append(f"Description curta ({desc_len} chars)")
                suggestions.append("Considere adicionar mais detalhes para melhor triggering")
        
        # Check "Use para:"
        if "Use para:" not in content:
            issues.append("Falta 'Use para:'")
            suggestions.append("Adicione seção 'Use para:' com contextos específicos")
        
        # Check "Não use para:"
        if "Não use para:" not in content:
            issues.append("Falta 'Não use para:'")
            suggestions.append("Adicione 'Não use para:' para evitar falsos positivos")
            
        # Check for examples
        if "## Examples" not in content and "### ✅ BOM" not in content:
            suggestions.append("Adicione exemplos (## Examples)")
        
        # Check for limitations
        if "## Limitations" not in content and "Limitations" not in content:
            suggestions.append("Adicione seção ## Limitations")
    
    else:
        # ChatGPT format (XML)
        if "<skill" not in content:
            issues.append("Falta tag <skill>")
        
        if "<pre_exec>" not in content:
            suggestions.append("Considere adicionar <pre_exec> para validação")
    
    return {
        "valid": len(issues) == 0,
        "issues": issues,
        "suggestions": suggestions
    }

def find_skill(skill_path: str) -> Path:
    """Encontra a skill em diferentes caminhos"""
    skill_path_obj = Path(skill_path)
    
    # Se é um caminho direto válido
    if skill_path_obj.exists():
        return skill_path_obj
    
    # Tentar em diferentes localizações
    paths_to_try = [
        SKILLS_ROOT / "prompts/web/claude" / skill_path,
        SKILLS_ROOT / "prompts/web/claude" / skill_path / "SKILL.md",
        SKILLS_ROOT / "prompts/web/chatgpt/skills" / skill_path,
    ]
    
    for path in paths_to_try:
        if path.exists():
            return path
    
    # Se não encontrar, retorna o original
    return skill_path_obj

def main():
    if len(sys.argv) < 2:
        print("🔍 Lovel Improve Description")
        print("=" * 50)
        print("\nUsage: python scripts/improve_description.py <skill>")
        print("\nExemplos:")
        print("  python scripts/improve_description.py hunting")
        print("  python scripts/improve_description.py outreach")
        sys.exit(1)
    
    skill_path = sys.argv[1]
    skill_full_path = find_skill(skill_path)
    result = analyze_description(str(skill_full_path))
    
    print("\n" + "=" * 50)
    print(f"📁 Skill: {skill_path}")
    print("=" * 50)
    
    if "error" in result:
        print(f"❌ {result['error']}")
        sys.exit(1)
    
    if result["issues"]:
        print(f"\n🔴 Problemas encontrados ({len(result['issues'])}):")
        for issue in result["issues"]:
            print(f"   ❌ {issue}")
    
    if result["suggestions"]:
        print(f"\n💡 Sugestões de melhoria ({len(result['suggestions'])}):")
        for suggestion in result["suggestions"]:
            print(f"   💡 {suggestion}")
    
    if not result["issues"] and not result["suggestions"]:
        print("\n✅ Skill está otimizada!")
    
    print()

if __name__ == "__main__":
    main()
