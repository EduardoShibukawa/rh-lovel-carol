---
name: skill-tester
description: "Testar, validar e melhorar skills de qualquer projeto. Use para: 
(1) Executar evals em skills, (2) Validar fixtures com CUE, (3) Melhorar estrutura de skills.
Não use para: criar skills do zero."
allowed_tools:
  - bash
---

# SKILL TESTER

Skill agnóstico para testar e validar skills de qualquer projeto usando CUE.

## Estrutura de Projetos

```
projects/
├── lovel/
│   └── skills/
│       ├── claude/
│       │   ├── hunting/
│       │   └── outreach/
│       └── chatgpt/
│           ├── hunting/
│           └── outreach/
└── conectacareer/
    └── skills/
        └── linkedin-post/
```

## Validação com CUE

Cada skill tem fixtures em `evals/testes.cue` com validação declarativa.

### Rodar Validação

```bash
# Validar fixtures de uma skill
cue vet -c projects/<projeto>/skills/claude/<skill>/evals/testes.cue

# Todas as skills de um projeto
python scripts/run_eval.py --project lovel

# Skill específica
python scripts/run_eval.py --project lovel --skill hunting

# Todos os projetos
python scripts/run_eval.py --all
```

## Scripts Disponíveis

```bash
# Executar evals (via CUE)
python scripts/run_eval.py --project <nome>

# Validar estrutura de skills
python scripts/quick_validate.py

# Melhorar description
python scripts/improve_description.py <skill>
```

## Fluxo de Teste

```
1. Editar skill em projects/<projeto>/skills/<platform>/<skill>/
2. Validar fixtures CUE: cue vet -c .../evals/testes.cue
3. Se falhar: ajustar fixtures ou skill
4. Executar evals: python scripts/run_eval.py --project <projeto>
5. Iterar até 90%+ pass rate
```

## Iteration Loop

1. Aplique melhorias na skill
2. Rerun `cue vet` para validar fixtures
3. Execute evals
4. Itere até satisfação

**Critérios de parada:**
- 90%+ pass rate
- Sem progresso em 3 iterações

## Limitations

- NÃO criar skills do zero
- NÃO ignore erros de CUE
- NÃO faça overfitting nos fixtures
- SEMPRE documente mudanças
