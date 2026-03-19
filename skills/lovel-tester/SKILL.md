---
name: lovel-tester
description: "Testar, validar e melhorar skills Lovel. Use para: (1) Executar evals em skills,
(2) Validar fixtures com CUE, (3) Melhorar skills, (4) Iterar até satisfação.
Não use para: criar skills do zero."
allowed_tools:
  - bash
  - validate_skill
---

# LOVEL TESTER

Skill para testar e validar skills Lovel de forma determinística usando CUE.

## Validação com CUE

Cada skill tem fixtures de teste em `evals/testes.cue` com validação declarativa.

### Rodar Validção

```bash
# Uma skill específica
cue vet -c prompts/web/claude/<skill>/evals/testes.cue

# Todas as skills (Claude)
for skill in hunting outreach post parecer; do
  cue vet -c prompts/web/claude/$skill/evals/testes.cue && echo "✅ $skill" || echo "❌ $skill"
done

# Todas as skills (ChatGPT)
for skill in hunting outreach post parecer; do
  cue vet -c prompts/web/chatgpt/skills/$skill/evals/testes.cue && echo "✅ $skill" || echo "❌ $skill"
done
```

### Scripts Disponíveis

```bash
# Todas as skills + plataformas
python scripts/run_eval.py all

# Skill específica
python scripts/run_eval.py <skill>

# Validar estrutura
python scripts/quick_validate.py <skill>
```

## Skills Disponíveis

| Skill | Path Claude | Path ChatGPT |
|-------|------------|--------------|
| hunting | prompts/web/claude/hunting/ | prompts/web/chatgpt/skills/hunting/ |
| outreach | prompts/web/claude/outreach/ | prompts/web/chatgpt/skills/outreach/ |
| post | prompts/web/claude/post/ | prompts/web/chatgpt/skills/post/ |
| parecer | prompts/web/claude/parecer/ | prompts/web/chatgpt/skills/parecer/ |

## Fluxo de Teste

```
1. Editar prompt/skills em prompts/web/
2. Validar fixtures: cue vet -c <skill>/evals/testes.cue
3. Se falhar: ajustar fixtures ou prompt
4. Executar evals via LLM: python scripts/run_eval.py <skill>
5. Iterar até 90%+ pass rate
```

## Iteration Loop

1. Aplique melhorias na skill
2. Rerun `cue vet` para validar fixtures
3. Execute evals via LLM
4. Itere até satisfação

**Critérios de parada:**
- 90%+ pass rate
- Feedback vazio
- Sem progresso em 3 iterações

## Limitations

- NÃO criar skills do zero
- NÃO ignore erros de CUE
- NÃO faça overfitting nos fixtures
- SEMPRE documente mudanças
