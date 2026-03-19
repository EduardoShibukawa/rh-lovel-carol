"""
Lovel Skill Validators.

Este módulo contém validadores determinísticos para cada skill.
O código NUNCA entra no contexto da LLM - apenas o output JSON.

Usage:
    from validators.dynamic_validator import validate
    
    result = validate('hunting', output_string)
    # Returns: {"valid": bool, "score": int, "issues": []}

Available validators:
    - validate_hunting: Boolean queries, X-Ray, NOT exclusions
    - validate_outreach: M1/M2 structure, character limits
    - validate_post: Hooks, salary, separators
    - validate_parecer: Structure, recommendation, PT-BR

Example:
    >>> from validators.dynamic_validator import validate
    >>> result = validate('hunting', '(Go OR Golang) AND (AWS)')
    >>> print(result)
    {'valid': True, 'score': 10, 'issues': []}
"""

from .dynamic_validator import (
    validate,
    validate_hunting,
    validate_outreach,
    validate_post,
    validate_parecer,
    VALIDATORS,
)

__all__ = [
    'validate',
    'validate_hunting',
    'validate_outreach',
    'validate_post',
    'validate_parecer',
    'VALIDATORS',
]
