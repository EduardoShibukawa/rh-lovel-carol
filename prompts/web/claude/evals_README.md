# Evals - Testes para Skills

Este diretório contém testes automatizados para validar as skills seguindo o padrão da skill-creator da Anthropic.

## Estrutura

```
skill/
├── SKILL.md
└── evals/
    └── evals.json
```

## Como Rodar Testes

### Usando skill-creator
1. Carregar a skill `skill-creator`
2. Executar os evals com: `run_eval` ou similar

### Teste Manual
Para cada eval:
1. Ler o prompt
2. Executar a skill
3. Verificar se o output atende o `expected_output`

## Evals por Skill

### lovel-hunting
| ID | Prompt | Verificação |
|----|--------|-------------|
| 1 | Go/Golang Senior | 5+ sinônimos, X-Ray |
| 2 | SDR/BDR Curitiba | ICP, Seed/Net/Spear |
| 3 | QA Engineer Playwright | Sinônimos, X-Ray |

### lovel-outreach
| ID | Prompt | Verificação |
|----|--------|-------------|
| 1 | M1 SDR | < 300 chars |
| 2 | M1 Developer | M1+M2, salary faixa |
| 3 | Follow-up Day 4 | Dia correto, emoji |

### lovel-post
| ID | Prompt | Verificação |
|----|--------|-------------|
| 1 | Vaga Go Senior | Hook 90 dias |
| 2 | 3 vagas | Hooks variados |
| 3 | Salary único | Converte para faixa |

### lovel-parecer
| ID | Prompt | Verificação |
|----|--------|-------------|
| 1 | Levi Alves QA | Estrutura completa |
| 2 | Jason Pires Tech Lead | Offer versão curta |

## Formato evals.json

```json
{
  "skill_name": "nome-da-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "Prompt de teste",
      "expected_output": "O que esperar do output"
    }
  ]
}
```
