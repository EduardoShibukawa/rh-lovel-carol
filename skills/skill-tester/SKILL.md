---
name: skill-tester
description: "Testar, validar e melhorar skills de qualquer projeto. Use para: 
(1) Validar fixtures com CUE (determinístico), (2) Avaliar qualidade subjetiva (LLM),
(3) Melhorar estrutura de skills.
Não use para: criar skills do zero."
allowed_tools:
  - bash
---

# SKILL TESTER

Skill agnóstico para testar e validar skills de qualquer projeto.

## Validação em Duas Camadas

### 1. Determinística (validate.py)
Verifica se fixtures CUE estão corretos (regras cumpridas).

### 2. Subjetiva (assess.py)
Avalia qualidade do prompt via LLM (clareza, tom, estrutura).

## Scripts Disponíveis

```bash
# Validação determinística (CUE fixtures)
python scripts/validate.py --project lovel
python scripts/validate.py --project lovel --skill hunting
python scripts/validate.py --all

# Avaliação subjetiva (LLM)
python scripts/assess.py --project lovel --skill hunting
python scripts/assess.py --project lovel
python scripts/assess.py --all

# Estrutura de skill
python scripts/quick_validate.py

# Melhorar description
python scripts/improve_description.py <skill>
```

## Estrutura de Projetos

```
projects/
├── lovel/
│   └── skills/
│       ├── claude/
│       │   ├── hunting/
│       │   └── outreach/
│       └── chatgpt/
│           └── hunting/
└── conectacareer/
    └── skills/
        └── linkedin-post/
```

## Fluxo de Teste

```
1. Editar skill em projects/<projeto>/skills/<platform>/<skill>/
2. Validar deterministicamente: python scripts/validate.py --project <projeto>
3. Se falhar: ajustar fixtures
4. Avaliar subjetivamente: python scripts/assess.py --project <projeto>
5. Se necessário: ajustar prompt
6. Iterar até 90%+ pass rate
```

## Avaliação Subjetiva (assess.py)

Avalia em 5 dimensões:
- **Clareza** - Instruções claras e objetivas?
- **Exemplos** - Bons e representativos?
- **Tom** - Humano, direto, não formal?
- **Estrutura** - Lógica e fácil de seguir?
- **Completude** - Todas informações necessárias?

Retorna scores 1-10 e sugestões de melhoria.

## Limitations

- NÃO criar skills do zero
- NÃO ignore erros de CUE
- NÃO faça overfitting nos fixtures
- SEMPRE documente mudanças
