---
name: lovel-tester
description: "Testar e validar as skills do projeto. Use para: (1) Executar evals em skills, 
(2) Validar critérios automaticamente, (3) Gerar benchmarks, (4) Comparar versões, 
(5) Verificar triggering. Não use para: criar ou editar skills."
---

# SKILL TESTER - Validação de Skills

Skill para testar, validar e medir performance das skills do projeto rh-carol, seguindo a metodologia da skill-creator.

## Overview

Executa testes automatizados para validar que as skills funcionam corretamente, seguem as autoridades e produzem outputs de qualidade.

## Autoridades Aplicadas

- **skill-creator**: Evals, benchmarks, comparator
- **Test-Prompt**: TDD para instruções LLM
- **Maxim AI**: Side-by-side comparison

---

## Workflow

### Passo 1: Detectar Mudanças
Executar para identificar o que mudou:
```bash
git diff --name-only tests_prompts/
```

### Passo 2: Selecionar Evals
Mapeamento skill → evals:
- `lovel-hunting` → usar `hunting/evals/evals.json`
- `lovel-outreach` → usar `outreach/evals/evals.json`
- `lovel-post` → usar `post/evals/evals.json`
- `lovel-parecer` → usar `parecer/evals/evals.json`

### Passo 3: Executar Evals
Para cada eval:
1. Ler o prompt de teste
2. Carregar a skill correspondente
3. Executar a skill com os dados do eval
4. Comparar output com expected_output
5. Registrar resultado

### Passo 4: Validar Critérios
Verificar automaticamente:
- Formato correto
- Autoridades aplicadas
- Tom e voz
- Limites (300 chars, 5+ sinônimos, etc)

### Passo 5: Gerar Relatório
Criar relatório com:
- Score (X/Y critérios)
- Status: APROVADO / REPROVADO / RESSALVAS
- Problemas identificados
- Recomendação

---

## Evals por Skill

### lovel-hunting
| ID | Prompt | Expected |
|----|--------|----------|
| 1 | Go/Golang Senior em fintech | 5+ sinônimos, X-Ray |
| 2 | SDR/BDR Curitiba | ICP, Seed/Net/Spear |
| 3 | QA Engineer Playwright | Sinônimos, X-Ray |

### lovel-outreach
| ID | Prompt | Expected |
|----|--------|----------|
| 1 | M1 para SDR | < 300 chars |
| 2 | M1 para Developer | M1 + M2 |
| 3 | Follow-up Day 4 | Dia correto |

### lovel-post
| ID | Prompt | Expected |
|----|--------|----------|
| 1 | Vaga Go Senior | Hook 90 dias |
| 2 | 3 vagas | Hooks variados |
| 3 | Salary único | Converte faixa |

### lovel-parecer
| ID | Prompt | Expected |
|----|--------|----------|
| 1 | Levi Alves QA | Estrutura completa |
| 2 | Jason Pires Tech Lead | Offer versão curta |

---

## Validação Automática

### Para TODAS as skills:
- [ ] Formato seguido corretamente?
- [ ] Tom humano, sem formalismo?
- [ ] Salary em faixa explícita?
- [ ] Autoridades aplicadas?
- [ ] Invite sugerido (com aviso)?

### lovel-hunting específico:
- [ ] Mínimo 5 sinônimos por termo?
- [ ] X-Ray search presente?
- [ ] Exclusões (NOT) para júnior/estágio?
- [ ] Localização específica (cidade + estado)?

### lovel-outreach específico:
- [ ] M1 máximo 300 caracteres?
- [ ] M2 com salary faixa?
- [ ] Follow-ups Day 4 e Day 7?
- [ ] Máximo 1 emoji por mensagem?

### lovel-post específico:
- [ ] Hook com impacto de 90 dias?
- [ ] Salary em faixa explícita?
- [ ] Máximo 4 vagas por post?
- [ ] Sem separadores ou travessões?

### lovel-parecer específico:
- [ ] Estrutura completa (resumo, experiência, stack, pontos)?
- [ ] Recomendação clara?
- [ ] Offer de versão curta?

---

## Formato do Relatório

```
📊 TESTE AUTOMÁTICO - [SKILL]

Eval: [ID] - [nome]
Prompt: [prompt de teste]
Expected: [critério esperado]
Result: ✅ PASSOU / ❌ FALHOU

Score: X/Y critérios
Status: [APROVADO/REPROVADO/RESSALVAS]

Problemas:
- [problema 1]
- [problema 2]

Recomendação: [aplicar ao projeto / revisar skill]
```

---

## Exemplos

### Execução de Eval
```
Eval: 1 - Go/Golang Senior
Prompt: "Boolean para Go/Golang Senior em fintech, São Paulo"
Expected: "5+ sinônimos, X-Ray, exclusões"

Resultado:
✅ 5 sinônimos: Go, Golang, Go language, Go developer, Gopher
✅ X-Ray: site:linkedin.com/in/ "Go" "São Paulo"
✅ Exclusões: NOT júnior, junior, trainee
✅ Localização: São Paulo, SP, Região Metropolitana

Score: 4/4
Status: ✅ APROVADO
```

### Comparação A/B
```
Versão A (sem skill):
- Output genérico
- Sem sinônimos

Versão B (com skill):
- Boolean completo
- 5+ sinônimos

Resultado: Versão B é significativamente melhor
```

---

## Limitations

- **PROIBIDO**: Modificar skills durante teste
- **PROIBIDO**: Ignorar critérios de validação
- **SEMPRE**: Reportar score honesto
- **SEMPRE**: Incluir problemas encontrados

## Validation

- [ ] Evals executados para todas as skills modificadas?
- [ ] Score reportado honestamente?
- [ ] Problemas claramente identificados?
- [ ] Recomendação clara?
