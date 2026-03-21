# AGENTS.md - Lovel Tech Recruiting Prompt System

This repository manages prompt engineering for a tech recruiting operation (Lovel/Carol Lima). It contains hunting, outreach, posting, and candidate evaluation prompts for multiple LLM platforms.

---

## Project Structure

```
rh-carol/
├── projects/lovel/skills/              # Main skills directory
│   ├── claude/                         # Claude.ai skills (YAML format)
│   │   ├── hunting/SKILL.md           # Boolean query generation
│   │   ├── outreach/SKILL.md          # DM personalization
│   │   ├── post/SKILL.md              # LinkedIn posts
│   │   ├── parecer/SKILL.md           # Candidate evaluation
│   │   └── */evals/testes.cue         # CUE fixtures for testing
│   └── chatgpt/                        # ChatGPT skills (XML format)
│       ├── skill_hunting.md
│       ├── skill_outreach.md
│       ├── skill_post.md
│       ├── skill_parecer.md
│       └── */evals/testes.cue
├── skills/skill-tester/scripts/         # Testing infrastructure (Python)
│   ├── quick_validate.py              # Structure validation
│   ├── run_eval.py                    # CUE fixtures validator (legacy)
│   ├── test_skill.py                  # LLM-based skill tester (NEW)
│   ├── validate.py                    # CUE fixtures validator
│   ├── assess.py                      # LLM-based quality assessment
│   └── llm_client.py                  # OpenCode API client
├── fixtures/                          # Test fixtures (PDFs, markdown)
└── AGENTS.md                          # This file
```

---

## Build/Lint/Test Commands

### LLM Skill Tester (NEW - Recommended)

```bash
# Test single skill with LLM
python skills/skill-tester/scripts/test_skill.py --project lovel --skill hunting

# Test all skills for a project
python skills/skill-tester/scripts/test_skill.py --project lovel

# Verbose output with detailed checks
python skills/skill-tester/scripts/test_skill.py --project lovel --skill hunting --verbose

# Test specific skill across all projects
python skills/skill-tester/scripts/test_skill.py --skill hunting
```

### CUE Fixtures Validator

```bash
# Validate specific fixture
cue vet projects/lovel/skills/claude/hunting/evals/testes.cue

# Validate all fixtures (Python)
python skills/skill-tester/scripts/validate.py --project lovel --skill hunting
python skills/skill-tester/scripts/validate.py --all
```

### Quick Structure Validation

```bash
# Validate all skills structure
python skills/skill-tester/scripts/quick_validate.py

# Validate specific skill
python skills/skill-tester/scripts/quick_validate.py --project lovel --skill hunting

# Validate specific platform
python skills/skill-tester/scripts/quick_validate.py --platform claude
```

---

## Test Workflow

The `test_skill.py` script performs end-to-end prompt testing:

1. **Load Skill Prompt** - Reads `SKILL.md` from the skill directory
2. **Load Fixtures** - Reads test cases from `evals/testes.cue`
3. **Call LLM** - Sends prompt + fixture input to OpenCode (Claude)
4. **Grade Output** - Applies skill-specific grading criteria
5. **Report** - Shows score (0-10), pass/fail, and detailed issues

### Grading Criteria by Skill

| Skill | Checks |
|-------|--------|
| **hunting** | No emoji, 5+ synonyms, X-Ray with site:linkedin.com/in, NOT exclusions, salary format |
| **outreach** | M1 ≤200 chars, M2 with salary, max 1 emoji, follow-up day 4/7, invite |
| **post** | Salary range, 90-day impact hook, invite, no em-dash |
| **parecer** | Resumo, stack, pontos, recomendação |

---

## Code Style Guidelines

### Python Scripts

**Imports** (standard library preferred):
```python
import argparse
import json
import re
import statistics
import subprocess
import sys
import time
from pathlib import Path
from typing import Dict, List, Any, Optional
```

**Type Hints**:
```python
def validate_skill_structure(skill_path: Path) -> dict[str, Any]:
    """Validate skill structure and return results."""
```

**Naming Conventions**:
- Functions/variables: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Type variables: `PascalCase` (e.g., `Dict`, `List`)

**Error Handling**:
- Return dict with `{"valid": bool, "errors": [], "warnings": []}`
- Use `sys.exit(1)` only for fatal CLI errors
- Print emojis for status: `✅` `❌` `⚠️` `📋`

---

### Markdown Prompts (YAML/Claude Format)

**Required Frontmatter**:
```yaml
---
name: lovel-hunting
description: "A short description for triggering (50+ chars)"
Use para: Contexts where this skill applies
Não use para: What to avoid
---
```

**Content Rules**:
- NO em-dashes (`—`) - use regular hyphens or en-dashes for ranges
- NO corporate jargon ("dinâmico", "oportunidade incrível", "empresa líder")
- LOVEL TONE: Conversational, direct, human. Avoid "RHzês" and formalisms
- Salary as range with en-dash: "R$ 10k – R$ 14k"
- Keep paragraphs short (3-4 lines max)
- Use numbered lists for steps
- Include `## Examples` section

---

### CUE Fixtures Format

Fixtures define test inputs for eval runner:

```cue
#HuntingTest: {
    id:       int
    prompt:   string
    expected: {
        techStack: string
        level:     string
        salary:    string
        location:  string
    }
}

testes: [
    (#HuntingTest & {
        id:     1
        prompt: "Boolean para Dev Go Sr - R$15k-22k - remoto - Go, Kubernetes"
        expected: {
            techStack: "Go"
            level:     "Senior"
            salary:    "R$ 15k – R$ 22k"
            location:  "Remoto"
        }
    }),
]
```

---

## Development Workflow

1. **Edit prompts** in `projects/lovel/skills/claude/` or `projects/lovel/skills/chatgpt/`
2. **Validate structure**: `python skills/skill-tester/scripts/quick_validate.py`
3. **Test with LLM**: `python skills/skill-tester/scripts/test_skill.py --project lovel --skill hunting --verbose`
4. **Iterate until 90%+ pass rate**

---

## Authorities & References

| Authority | Principle |
|-----------|-----------|
| Lou Adler | Performance-based Hiring |
| Stacy Zapar | 3x3 Rule |
| Glen Cathey | Boolean Black Belt |
| Aaron Ross | Predictable Revenue |
| Gergely Orosz | Pragmatic Engineer |

---

## Project Metrics

| Skill | Claude | ChatGPT | Avg Score |
|-------|--------|---------|-----------|
| hunting | 10.0 | 10.0 | **10.0** |
| outreach | 10.0 | 10.0 | **10.0** |
| post | 10.0 | 10.0 | **10.0** |
| parecer | 10.0 | 10.0 | **10.0** |

**Overall: 10.0/10** | **Backend**: OpenCode (Claude 3.7 Sonnet)

---

**Last Updated**: 2026-03-19
