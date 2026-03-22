# AGENTS.md - Lovel Tech Recruiting Prompt System

This repository manages prompt engineering for a tech recruiting operation. It contains hunting, outreach, posting, and candidate evaluation prompts for multiple LLM platforms.

---

## Autoridades em Prompt Engineering

### Core Authorities

| Authority | Princípio | Fonte |
|-----------|------------|-------|
| **Anthropic** | XML tags para estrutura (15-20% melhor), few-shot examples, context engineering | anthropic.com |
| **OpenAI** | 6 estratégias: instruções claras, referência, decomposição, exemplos, CoT, avaliação | platform.openai.com |
| **PE Collective** | Priority stack, estrutura: identity, rules, format, edge cases, examples | pecollective.com |
| **Field Guide to AI** | 6 camadas: identity, context, instructions, format, edge cases, defensive | fieldguidetoai.com |
| **Azure/Microsoft** | Be specific, be descriptive, order matters | docs.microsoft.com |

### Recruiting Authorities

| Authority | Princípio | Fonte |
|-----------|-----------|-------|
| **Lou Adler** | Performance-based Hiring, impacto de 90 dias | louadler.com |
| **Stacy Zapar** | 3x3 Rule, cadência de outreach | stacyzapar.com |
| **Glen Cathey** | Boolean Black Belt | booleanblackbelt.com |
| **Aaron Ross** | Predictable Revenue | predictablerevenue.com |
| **Gergely Orosz** | Pragmatic Engineer, tech challenges | newsletter.pragmaticengineer.com |

---

## Princípios de Prompt Engineering (Baseado em Pesquisa)

### 1. Estrutura P-TFC

```
P - Prompt (instruções)
T - Task (tarefa)
F - Format (formato de saída)
C - Constraints (regras/restrições)
```

### 2. Few-Shot > Muitas Instruções

Exemplos mostram melhor que explicações:
- 2-4 exemplos (1 normal, 1 edge case)
- Mostram comportamento esperado

### 3. Priority Stack

Quando regras conflitam, definir prioridade:
```
Priority 1 (never violate): Safety, compliance
Priority 2 (strong preference): Accuracy
Priority 3 (default): Tone, format
```

### 4. XML Tags para Claude

```xml
<prompt>
  <role>Você é um recruiter...</role>
  <task>Gerar boolean query...</task>
  <format>
    ## ICP
    ...
  </format>
  <constraints>
    - Zero emojis
    - 5+ sinônimos
  </constraints>
  <examples>
    <example id="1">
      <input>...</input>
      <output>...</output>
    </example>
  </examples>
</prompt>
```

### 5. Edge Cases Explícitos

Sempre incluir:
- O que fazer quando info está ausente
- O que fazer quando ambiguous
- Fallback behavior

---

## Project Structure

```
rh-carol/
├── projects/
│   └── lovel/
│       └── skills/
│           ├── claude/                     # Skills (YAML format)
│           │   ├── hunting/SKILL.md
│           │   ├── outreach/SKILL.md
│           │   ├── post/SKILL.md
│           │   ├── parecer/SKILL.md
│           │   └── */evals/testes.cue
│           └── chatgpt/                   # Skills (XML format)
│               └── skill_*.md
├── skills/
│   └── skill-tester/                     # Testing infrastructure
│       └── scripts/
│           ├── test.py                    # Deterministic + Subjective
│           ├── validate.py                 # CUE validation
│           ├── assess.py                  # LLM assessment
│           └── llm_client.py
└── fixtures/                            # Test fixtures
```

---

## Build/Lint/Test Commands

### Testing (Recommended)

```bash
# Combined: deterministic + subjective
python skills/skill-tester/scripts/test.py --project lovel --skill hunting
python skills/skill-tester/scripts/test.py --project lovel

# Deterministic only (CUE fixtures)
python skills/skill-tester/scripts/validate.py --project lovel

# Subjective only (LLM assessment)
python skills/skill-tester/scripts/assess.py --project lovel
```

### Legacy Commands

```bash
python skills/skill-tester/scripts/quick_validate.py
python skills/skill-tester/scripts/run_eval.py hunting
```

---

## Code Style Guidelines

### Python Scripts

**Imports (stdlib only):**
```python
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Any
```

**Type Hints:**
```python
def validate_skill(skill_path: Path) -> dict[str, Any]:
    """Docstring describing function."""
```

**Naming:**
- snake_case: functions, variables
- PascalCase: classes
- UPPER_SNAKE_CASE: constants

**Error Handling:**
- Return `{"valid": bool, "errors": [], "warnings": []}`
- sys.exit(1) only for fatal CLI errors

### Markdown Prompts (Claude/YAML format)

**Frontmatter:**
```yaml
---
name: lovel-hunting
description: "Boolean queries, X-Ray search, sourcing ativo..."
Use para: Contexts where this skill applies
Não use para: What to avoid
---
```

**Content Rules:**
- NO em-dashes (`—`) - use en-dash (`–`) for ranges
- NO corporate jargon ("dinâmico", "oportunidade incrível")
- TOM: Conversational, direct, human
- Salary as range: "R$ 10k – R$ 14k"
- Keep paragraphs short (3-4 lines)
- Use numbered lists for steps
- Include `## Examples` section

---

## Development Workflow

1. **Edit prompts** in `projects/lovel/skills/claude/<skill>/`
2. **Validate fixtures**: `cue vet -c .../testes.cue`
3. **Test combined**: `python skills/skill-tester/scripts/test.py --project lovel`
4. **Iterate** until 9.5+ in all dimensions
5. **Commit** changes

---

## Test Criteria by Skill

### Hunting (Boolean Queries)
- 5+ synonyms per tech term
- X-Ray search (site:linkedin.com/in)
- NOT exclusions for junior/intern
- Location specificity
- ZERO emojis

### Outreach (DM Templates)
- M1 max 200 characters
- M2 with explicit salary range
- Follow-up: Day 4 / Day 7
- Invite parameter: `invite=caroline.lima798`
- Max 1 emoji per message

### Post (LinkedIn)
- Hook with 90-day impact (not job title)
- Explicit salary range
- Max 4 jobs per post
- No separators/em-dashes
- Max 1 emoji per line

### Parecer (Candidate Evaluation)
- Structure: Resumo, Experiência, Stack, Pontos, Recomendação
- ZERO emojis
- PT-BR only (tech terms accepted)
- Specific, not generic points

---

## Validation Dimensions (assess.py)

| Dimension | Description | Target |
|-----------|-------------|--------|
| Clareza | Instruções claras e objetivas | 9.5+ |
| Exemplos | Bons e representativos | 9.5+ |
| Tom | Humano, direto, não formal | 9.5+ |
| Estrutura | Lógica e fácil de seguir | 9.5+ |
| Completude | Todas informações necessárias | 9.5+ |

---

**Last Updated**: 2026-03-22
