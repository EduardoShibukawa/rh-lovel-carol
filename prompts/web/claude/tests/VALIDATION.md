# VALIDAÇÃO DE SKILLS - Critérios por Autoridade

## Stacy Zapar (OUTREACH)
| Critério | Limite | Como Validar |
|----------|--------|---------------|
| M1 | **200 chars** | Contar caracteres |
| Emoji | 1 por mensagem | Verificar contagem |
| Follow-up | Day 4 / Day 7 | Presença |

## Lou Adler (POST)
| Critério | Como Validar |
|----------|---------------|
| Hook = impacto | Ver se não é cargo |
| 90 dias | Mencionar resultado mensurável |
| Career growth | "30% mais desafio" (opcional) |

## Glen Cathey (HUNTING)
| Critério | Limite | Como Validar |
|----------|--------|---------------|
| Sinônimos | **5+** por termo | Contar ORs |
| X-Ray | site:linkedin.com/in | Buscar no output |
| Exclusões | NOT júnior/estágio | Verificar NOT |
| Localização | Cidade + estado + região | Verificar ORs |

## Aaron Ross (HUNTING - Comercial)
| Critério | Como Validar |
|----------|---------------|
| ICP | Presença de hipóteses |
| Seed/Net/Spear | Conceito mencionado |

## Gergely Orosz (POST/HUNTING)
| Critério | Como Validar |
|----------|---------------|
| Senioridade | Autonomia/impacto, não tempo de casa |
| Tech stack | Desafios específicos |

## Lovel (TODAS)
| Critério | Como Validar |
|----------|---------------|
| Salary | Faixa explícita (R$ Xk – R$ Yk) |
| Invite | invite=caroline.lima798 |
| Tom | Sem formalismo |

---

## Test Runner

### Para testar uma skill:
1. Carregar SKILL.md da skill
2. Usar fixture em tests/fixtures/
3. Gerar output
4. Validar contra critérios acima

### Exemplo de validação (HUNTING):
```
Input: vaga_go.md
Output esperado: Boolean com 5+ sinônimos, X-Ray, exclusões
Validação: 
  - [ ] 5+ sinônimos para "Go"? → SIM
  - [ ] X-Ray presente? → SIM
  - [ ] NOT para júnior? → SIM
  - [ ] Localização específica? → SIM
```

### Exemplo de validação (OUTREACH):
```
Input: vaga_bdr.md  
Output esperado: M1 máx 200 chars
Validação:
  - [ ] M1 ≤ 200 chars? → SIM
  - [ ] M2 com salary faixa? → SIM
  - [ ] Follow-up Day 4/7? → SIM
  - [ ] Invite presente? → SIM
```
