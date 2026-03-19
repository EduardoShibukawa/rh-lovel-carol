#!/usr/bin/env python3
"""
Dynamic Validator - Core validation engine for Lovel Skills.

Este script valida outputs de skills de forma DETERMINÍSTICA.
O código NUNCA entra no contexto da LLM - apenas o output JSON.

Usage:
    python validators/dynamic_validator.py --skill <skill_name> --output "<output>"
    python validators/dynamic_validator.py --skill hunting --output "(Go OR Golang)"
    python validators/dynamic_validator.py --skill outreach --output "Oi João! Sou Carol..."

Args:
    --skill: Nome da skill a validar (hunting, outreach, post, parecer)
    --output: Output da skill a ser validado

Returns:
    JSON com: {"valid": bool, "score": int, "issues": []}

Examples:
    >>> python validators/dynamic_validator.py --skill hunting --output "(Go OR Golang) AND (AWS)"
    {"valid": true, "score": 10, "issues": []}
    
    >>> python validators/dynamic_validator.py --skill hunting --output "Go developer"
    {"valid": false, "score": 5, "issues": ["Falta X-Ray", "Menos de 5 sinônimos"]}
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional


# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))


def validate_hunting(output: str) -> Dict[str, Any]:
    """
    Valida output de hunting skill.
    
    Regras:
        - Boolean com 5+ sinônimos por termo
        - X-Ray site:linkedin.com/in
        - NOT exclusions
        - ZERO emojis
        - Salary R$ Xk – R$ Yk (en-dash)
    
    Returns:
        Dict com valid, score, issues
    """
    issues: List[str] = []
    score = 10
    
    # Check X-Ray
    if not re.search(r'site:linkedin\.com/in', output, re.IGNORECASE):
        issues.append("Falta X-Ray com site:linkedin.com/in")
        score -= 2
    
    # Check for emojis
    emoji_pattern = re.compile(
        "[\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F700-\U0001F77F"  # alchemical symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002702-\U000027B0"  # Dingbats
        "\U000024C2-\U0001F251"  # enclosed characters
        "]+"
    )
    if emoji_pattern.search(output):
        issues.append("Emoji encontrado - ZERO emojis permitido")
        score -= 3
    
    # Check for em-dashes
    if '—' in output:
        issues.append("Em-dash (—) encontrado - usar en-dash (–)")
        score -= 1
    
    # Check salary format
    if not re.search(r'R\$\s*\d+k?\s*–\s*R\$\s*\d+k', output, re.IGNORECASE):
        if not re.search(r'R\$\s*[\d,.]+\s*k?\s*–\s*R\$\s*[\d,.]+\s*k?', output):
            issues.append("Salary não está no formato R$ Xk – R$ Yk")
            score -= 2
    
    # Check for NOT exclusions
    not_pattern = r'NOT\s*\('
    if not re.search(not_pattern, output, re.IGNORECASE):
        issues.append("Falta NOT exclusions")
        score -= 2
    
    # Check for synonyms (at least 5 OR terms)
    or_count = len(re.findall(r'\bOR\b', output, re.IGNORECASE))
    if or_count < 5:
        issues.append(f"Poucos sinônimos ({or_count} < 5)")
        score -= 2
    
    # Check for location
    if not re.search(r'(São Paulo|SP|Brasil|Remoto|Híbrido|Presencial)', output, re.IGNORECASE):
        issues.append("Falta localização")
        score -= 1
    
    score = max(0, min(10, score))
    return {
        "valid": len(issues) == 0,
        "score": score,
        "issues": issues
    }


def validate_outreach(output: str) -> Dict[str, Any]:
    """
    Valida output de outreach skill.
    
    Regras (smart validation based on content):
        - M1: máx 200 caracteres, sem salary
        - M2: salary faixa, invite
        - Follow-up: Day 4 e Day 7
        - Máximo 1 emoji por mensagem
    
    Returns:
        Dict com valid, score, issues
    """
    issues: List[str] = []
    score = 10
    
    lines = output.split('\n')
    
    # Check if this is M1 (short message) or M2 (contains details)
    is_m1 = len(output) < 300 and 'perfeito' not in output.lower() and 'mais detalhes' not in output.lower()
    is_followup = 'day 4' in output.lower() or 'dia 4' in output.lower()
    
    # Check M1 character count (only for M1)
    if is_m1:
        m1_line = ""
        for line in lines[:5]:
            if 'oi' in line.lower() and '!' in line:
                m1_line = line
                break
        
        if m1_line:
            char_count = len(m1_line.strip())
            if char_count > 200:
                issues.append(f"M1 tem {char_count} caracteres (> 200)")
                score -= 2
    elif 'salary' in output.lower() or 'remunera' in output.lower() or 'r$' in output.lower():
        # M2 should have salary
        if not re.search(r'R\$\s*\d+k?\s*–\s*R\$\s*\d+k', output, re.IGNORECASE):
            if not re.search(r'R\$\s*[\d,.]+\s*k?\s*–\s*R\$\s*[\d,.]+\s*k?', output):
                issues.append("Salary não está no formato R$ Xk – R$ Yk")
                score -= 2
    
    # Check for emojis (max 1 per message)
    emoji_pattern = re.compile(
        "[\U0001F600-\U0001F64F"
        "\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF"
        "\U00002702-\U000027B0"
        "]+"
    )
    emojis_found = emoji_pattern.findall(output)
    if len(emojis_found) > 1:
        issues.append(f"Múltiplos emojis encontrados ({len(emojis_found)} > 1)")
        score -= 2
    
    # Check for invite parameter (in M2 or full outreach)
    if ('link' in output.lower() or '🔗' in output) and 'invite=' not in output.lower():
        issues.append("Falta invite parameter")
        score -= 1
    
    # Check for follow-up structure
    if 'day 4' in output.lower() or 'dia 4' in output.lower():
        if 'day 7' not in output.lower() and 'dia 7' not in output.lower():
            if not is_m1:  # Don't penalize M1 for missing Day 7
                issues.append("Falta follow-up Day 7")
                score -= 1
    
    score = max(0, min(10, score))
    return {
        "valid": len(issues) == 0,
        "score": score,
        "issues": issues
    }


def validate_post(output: str) -> Dict[str, Any]:
    """
    Valida output de post skill.
    
    Regras:
        - Hook com impacto (não cargo)
        - Salary faixa explícito
        - Sem separadores (---)
        - Máximo 4 vagas por post
        - Máximo 1 emoji por linha
    
    Returns:
        Dict com valid, score, issues
    """
    issues: List[str] = []
    score = 10
    
    # Check for em-dashes and separators
    if '---' in output or '===' in output:
        issues.append("Separador proibido (--- ou ===)")
        score -= 2
    
    # Check for em-dash
    if '—' in output:
        issues.append("Em-dash (—) encontrado - usar en-dash (–)")
        score -= 1
    
    # Check salary format
    if not re.search(r'R\$\s*\d+k?\s*–\s*R\$\s*\d+k', output, re.IGNORECASE):
        issues.append("Salary não está no formato R$ Xk – R$ Yk")
        score -= 2
    
    # Check for hook with impact (not job title)
    lines = output.split('\n')
    hook_lines = [l for l in lines if l.strip() and not l.strip().startswith(('💰', '📍', '🛠️', '🔗', '💡', 'R$'))]
    
    if hook_lines:
        first_hook = hook_lines[0].lower()
        # Check if it's a job title instead of impact
        if any(word in first_hook for word in ['senior', 'junior', 'pleno', 'engineer', 'developer', 'analista', 'desenvolvedor']):
            issues.append("Hook usa cargo ao invés de impacto")
            score -= 2
    
    # Check for emojis per line
    emoji_pattern = re.compile(
        "[\U0001F600-\U0001F64F"
        "\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF"
        "\U00002702-\U000027B0"
        "]+"
    )
    
    for i, line in enumerate(lines):
        emojis_in_line = emoji_pattern.findall(line)
        if len(emojis_in_line) > 1:
            issues.append(f"Linha {i+1} tem múltiplos emojis ({len(emojis_in_line)})")
            score -= 1
    
    # Check for "a combinar" in salary
    if 'a combinar' in output.lower() or 'à combinar' in output.lower():
        issues.append("Salary 'a combinar' proibido")
        score -= 3
    
    score = max(0, min(10, score))
    return {
        "valid": len(issues) == 0,
        "score": score,
        "issues": issues
    }


def validate_parecer(output: str) -> Dict[str, Any]:
    """
    Valida output de parecer skill.
    
    Regras:
        - Estrutura completa
        - Recomendação clara
        - Versão curta oferecida
        - ZERO emojis
        - PT-BR (exceto tecnologias)
    
    Returns:
        Dict com valid, score, issues
    """
    issues: List[str] = []
    score = 10
    
    output_lower = output.lower()
    
    # Check for emojis
    emoji_pattern = re.compile(
        "[\U0001F600-\U0001F64F"
        "\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF"
        "\U00002702-\U000027B0"
        "]+"
    )
    if emoji_pattern.search(output):
        issues.append("Emoji encontrado - ZERO emojis permitido")
        score -= 3
    
    # Check for non-PT-BR text (simplified check)
    # Look for common Chinese/Russian characters
    non_pt_chars = re.findall(r'[\u4e00-\u9fff\u0400-\u04ff]', output)
    if non_pt_chars:
        issues.append("Texto em idioma não-latino encontrado")
        score -= 3
    
    # Check for structure sections
    required_sections = [
        ('resumo', 'Resumo do perfil'),
        ('pontos fortes', 'Pontos fortes'),
        ('pontos de atenção', 'Pontos de atenção'),
        ('recomenda', 'Recomendação'),
    ]
    
    missing_sections = []
    for keyword, label in required_sections:
        if keyword not in output_lower:
            missing_sections.append(label)
    
    if missing_sections:
        issues.append(f"Seções faltando: {', '.join(missing_sections)}")
        score -= 2
    
    # Check for version curta offer
    if 'versão curta' not in output_lower and 'short version' not in output_lower:
        issues.append("Falta offer de versão curta")
        score -= 1
    
    # Check for recommendation
    if not re.search(r'\b(ok|recomendo|não recomendo|avançar)\b', output_lower):
        issues.append("Recomendação não está clara")
        score -= 1
    
    # Check for em-dash
    if '—' in output:
        issues.append("Em-dash (—) encontrado")
        score -= 1
    
    score = max(0, min(10, score))
    return {
        "valid": len(issues) == 0,
        "score": score,
        "issues": issues
    }


# Registry of validators
VALIDATORS = {
    'hunting': validate_hunting,
    'outreach': validate_outreach,
    'post': validate_post,
    'parecer': validate_parecer,
}


def validate(skill_name: str, output: str) -> Dict[str, Any]:
    """
    Main validation function.
    
    Args:
        skill_name: Nome da skill (hunting, outreach, post, parecer)
        output: Output da skill a ser validado
    
    Returns:
        Dict com valid, score, issues
    """
    validator = VALIDATORS.get(skill_name.lower())
    
    if not validator:
        return {
            "valid": False,
            "score": 0,
            "issues": [f"Skill '{skill_name}' não reconhecida"]
        }
    
    return validator(output)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Dynamic Validator for Lovel Skills",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python validators/dynamic_validator.py --skill hunting --output "(Go OR Golang) AND (AWS)"
    python validators/dynamic_validator.py --skill outreach --output "Oi João! Sou Carol da Lovel."
    python validators/dynamic_validator.py --skill post --output "🚀 Tornar API 3x mais rápida..."
    python validators/dynamic_validator.py --skill parecer --output "Resumo: Dev Senior..."
        """
    )
    
    parser.add_argument(
        '--skill',
        required=True,
        choices=['hunting', 'outreach', 'post', 'parecer'],
        help='Nome da skill a validar'
    )
    
    parser.add_argument(
        '--output',
        required=True,
        help='Output da skill a ser validado'
    )
    
    args = parser.parse_args()
    
    result = validate(args.skill, args.output)
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()
