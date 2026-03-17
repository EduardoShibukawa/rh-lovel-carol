---
name: lovel-tester
description: "Testar, validar e melhorar skills existentes. Use para: (1) Executar evals em skills,
(2) Melhorar skills com base em feedback, (3) Iterar até满意, (4) Comparar versões, (5) Otimizar triggering.
Não use para: criar novas skills do zero (use skill-creator)."
---

# LOVEL TESTER

Skill baseada na methodology da skill-creator da Anthropic.

## Fluxo

1. DETECTAR O QUE FAZER
2. CARREGAR SKILL
3. EXECUTAR EVALS
4. AVALIAR COM USUÁRIO
5. MELHORAR
6. ITERAR

## Skills Disponíveis

- hunting → prompts/web/claude/hunting/
- outreach → prompts/web/claude/outreach/
- post → prompts/web/claude/post/
- parecer → prompts/web/claude/parecer/

## Como Pensar Melhorias

1. GENERALIZE - não faça overfitting
2. MANTENHA LEVE - remova o que não contribui
3. EXPLIQUE O PORQUÊ - LLMs são smart
4. PROCURE REPETIÇÃO - signals para bundling

---

## Estrutura

```
skill/
├── SKILL.md
├── evals/
│   └── evals.json
├── references/
└── scripts/
```

---

## Iteration Loop

1. Aplique melhorias
2. Rerun test cases
3. Mostre resultados
4. Aguarde feedback
5. Repita

Continue até:
- Usuário feliz
- Feedback vazio
- Sem progresso

---

## Reference Files

- `references/schemas.md` - JSON schemas
- `agents/grader.md` - Como avaliar
- `agents/comparator.md` - Como comparar

---

## Limitations

- NÃO criar skills do zero
- NÃO ignore feedback
- NÃO overfitting
- SEMPRE documente

---

## Scripts

```bash
python scripts/quick_validate.py [skill]
python scripts/run_eval.py [skill]
python scripts/improve_description.py [skill]
```
