# AGENTS.md - Lovel Tech Recruiting Prompt System

This repository contains prompt engineering for a tech recruiting operation (Lovel/Carol Lima). It manages hunting, outreach, and posting prompts for multiple LLM platforms.

---

## 📁 Project Structure

```
rh-carol/
├── AGENTS.md                           # This file
├── prompts/
│   └── web/
│       ├── claude/                     # Claude.ai skills (YAML format)
│       │   ├── hunting/SKILL.md        # Boolean query generation
│       │   ├── outreach/SKILL.md       # DM personalization
│       │   ├── post/SKILL.md           # LinkedIn posts
│       │   ├── parecer/SKILL.md        # Candidate evaluation
│       │   ├── authorities/            # Reference principles
│       │   ├── system_prompt.md        # Main router
│       │   └── tests/                  # Manual test fixtures
│       └── chatgpt/                    # ChatGPT skills (XML format)
│           ├── skills/
│           └── evals/
└── skills/
    └── lovel-tester/                   # Testing infrastructure
        └── scripts/                    # Automation scripts
```

---

## 🚀 Opencode Integration

A skill `lovel-tester` está disponível no opencode global em `~/.opencode/skill/lovel-tester/`.

```bash
# Chame no opencode com:
/lovel-tester
```

Use para testar, validar e iterar nas skills do projeto.

### Validation Scripts (Python)

All scripts are in `skills/lovel-tester/scripts/`:

```bash
# Validate all skills structure
python skills/lovel-tester/scripts/quick_validate.py

# Validate specific skill
python skills/lovel-tester/scripts/quick_validate.py hunting

# Validate specific platform
python skills/lovel-tester/scripts/quick_validate.py claude

# Run evals for a skill
python skills/lovel-tester/scripts/run_eval.py hunting
python skills/lovel-tester/scripts/run_eval.py claude/hunting

# Analyze and suggest improvements for a skill
python skills/lovel-tester/scripts/improve_description.py hunting
```

### Manual Test Runner (Bash)

```bash
# From prompts/web/claude directory
cd prompts/web/claude

# Run test with fixture
./tests/test_runner.sh hunting vagas_tech
./tests/test_runner.sh outreach vaga_go
./tests/test_runner.sh post vaga_bdr

# List available fixtures
ls tests/fixtures/
```

---

## 📋 Code Style Guidelines

### Python Scripts

**Imports**
```python
import json
import sys
import re
from pathlib import Path
```

**Type Hints**
```python
def validate_skill_structure(skill_path: Path) -> dict:
    """Docstring describing function."""
```

**Naming**
- snake_case for functions/variables: `validate_skill_structure`
- PascalCase for classes (if any)
- Constants: UPPER_SNAKE_CASE

**Error Handling**
- Return dict with `{"valid": bool, "errors": [], "warnings": []}`
- Use sys.exit(1) only for fatal CLI errors
- Print emojis for status: ✅ ❌ ⚠️ 📋

### Markdown Prompts (YAML/Claude format)

**Required Frontmatter**
```yaml
---
name: lovel-hunting
description: "A short description for triggering (50+ chars)"
Use para: Contexts where this skill applies
Não use para: What to avoid
---
```

**Content Rules**
- NO em-dashes (`—`) - use regular hyphens or en-dashes for ranges
- NO corporate jargon ("dinâmico", "oportunidade incrível", "empresa líder", "perfil diferenciado")
- LOVEL TONE: Conversational, direct, and human. Avoid "RHzês" and formalisms.
- Salary always as range with en-dash: "R$ 10k – R$ 14k"
- Keep paragraphs short (3-4 lines max)
- Use numbered lists for steps
- Include "## Examples" section

### Markdown Prompts (XML/ChatGPT format)

```xml
<skill>
<name>skill_hunting</name>
<description>Description here</description>
<instructions>
1. Step one
2. Step two
</instructions>
<examples>
### ✅ BOM
Input: ...
Output: ...

### ❌ RUIM
Input: ...
Output: ...
</examples>
</skill>
```

---

## 🧪 Test Criteria by Skill

### Hunting (Boolean Queries)
- 5+ synonyms per tech term (MANDATORY)
- X-Ray search (site:linkedin.com/in)
- NOT exclusions for junior/intern
- Location specificity
- Emoji: ZERO (Hunting is a technical asset)

### Outreach (DM Templates)
- M1 max 200 characters
- M2 with explicit salary range
- Follow-up: Day 4 / Day 7
- Invite parameter: `invite=caroline.lima798`
- Emoji: Máximo 1 por mensagem (Strict)

### Post (LinkedIn)
- Hook with 90-day impact (not job title)
- Explicit salary range
- Max 4 jobs per post
- No separators/em-dashes
- Emoji: Máximo 1 por linha (ideal para bullet points)

---

## 🔄 Development Workflow

1. **Edit prompts** in `prompts/web/claude/` or `prompts/web/chatgpt/`
2. **Validate structure**: `python skills/lovel-tester/scripts/quick_validate.py`
3. **Run evals**: `python skills/lovel-tester/scripts/run_eval.py <skill>`
4. **Iterate until 90%+ pass rate**

---

## 📚 Authorities & References

| Authority | Principle |
|-----------|-----------|
| Lou Adler | Performance-based Hiring |
| Stacy Zapar | 3x3 Rule |
| Glen Cathey | Boolean Black Belt |
| Aaron Ross | Predictable Revenue |
| Gergely Orosz | Pragmatic Engineer |

---

## 📊 Project Metrics

| Skill | Pass Rate | Avg Score | Latency |
|-------|-----------|-----------|---------|
| hunting | 90% | 8.9/10 | 8.6s |
| outreach | TBD | TBD | TBD |
| post | TBD | TBD | TBD |
| parecer | TBD | TBD | TBD |

**Backend**: OpenCode (Claude 3.7 Sonnet) only - other backends not reliable for production.

---

**Last Updated**: 2026-03-18
