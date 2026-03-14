# TESTES - CLAUDE SKILLS

Este diretório contém testes automatizados para validar as skills no padrão Claude.ai Web.

## Estrutura

```
tests/
├── fixtures/          # Entradas de exemplo para validação
│   ├── vagas_tech.md
│   ├── vaga_bdr.md
│   └── vaga_go.md
└── results/           # Resultados esperados (golden sets)
    ├── hunting_result.md
    ├── outreach_result.md
    └── post_result.md
```

## Como Testar

### Teste Manual
1. Carregar a skill desejada
2. Aplicar a fixture como entrada
3. Validar output contra critérios

### Critérios de Validação por Skill

#### HUNTING
- [ ] Boolean com 5+ sinônimos
- [ ] X-Ray search (site:linkedin.com/in)
- [ ] Exclusões (NOT júnior/estágio)
- [ ] Localização específica

#### OUTREACH
- [ ] M1 máximo 200 caracteres
- [ ] M2 com salary faixa
- [ ] Follow-up Day 4 / Day 7
- [ ] Invite parameter

#### POST
- [ ] Hook com impacto 90 dias
- [ ] Salary faixa explícita
- [ ] Máximo 4 vagas por post
- [ ] Sem separadores/travessões
