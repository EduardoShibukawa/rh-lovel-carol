---
name: improve-skills
description: "Melhorar skills até 9.5+ na avaliação. Use para: (1) Avaliar skills com assess.py,
(2) Identificar issues, (3) Melhorar SKILL.md, (4) Rerodar até 9.5+.
Não use para: criar skills do zero."
---

# Melhorar Skills para 9.5+

## Contexto

Use assess.py para avaliar e melhorar as skills até 9.5+.

## Scores Alvo

| Skill | Atual | Meta |
|-------|-------|------|
| hunting | 8.8 | 9.5+ |
| outreach | 8.6 | 9.5+ |
| post | 8.8 | 9.5+ |
| parecer | 8.8 | 9.5+ |

## Fluxo de Melhoria

```
1. Avaliar skill atual:
   python skills/skill-tester/scripts/assess.py --project lovel --skill <skill>

2. Identificar issues no output

3. Editar SKILL.md em:
   projects/lovel/skills/claude/<skill>/SKILL.md

4. Rerodar assess.py para verificar

5. Repetir até 9.5+
```

## Issues a Corrigir

### hunting
- Adicionar "Perguntas iniciais" para coletar info da vaga
- Incluir como definir salary range
- Adicionar 2-3 exemplos com stacks diferentes

### outreach
- Adicionar exemplo de personalização
- Incluir invite=no link: `?invite=caroline.lima798`

### post
- Adicionar exemplo visual de hífen (-) vs en-dash (–)
- Incluir hooks por setor (fintech, healthtech, SaaS)

### parecer
- Adicionar guideline para perfis incompletos
- Incluir critérios: Jr 0-2, Pl 2-4, Sr 4-7

## Scripts

```bash
# Avaliar uma skill
python skills/skill-tester/scripts/assess.py --project lovel --skill hunting

# Todas as skills
python skills/skill-tester/scripts/assess.py --project lovel

# Validar fixtures
python skills/skill-tester/scripts/validate.py --project lovel
```

## Critério

A skill está pronta quando:
- assess.py retornar 9.5+ em todas as dimensões
- Não houver issues ou suggestions críticas
