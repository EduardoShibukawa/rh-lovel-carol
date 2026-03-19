# Lovel Grader - Avaliação de Skills

Avalie se a resposta segue TODAS as regras da skill.

## Regras por Skill

### HUNTING
- ✅ 5+ sinônimos por termo técnico
- ✅ X-Ray com site:linkedin.com/in
- ✅ NOT exclusions (júnior/trainee)
- ✅ ZERO emojis
- ✅ Salary R$ Xk – R$ Yk (en-dash)

### OUTREACH
- ✅ M1 máx 200 caracteres
- ✅ M2 com salary faixa
- ✅ Follow-up Day 4 e Day 7
- ✅ Máximo 1 emoji por mensagem
- ✅ Invite: caroline.lima798

### POST
- ✅ Hook com impacto (não cargo)
- ✅ Salary faixa explícito
- ✅ Máximo 4 vagas por post
- ✅ Máximo 1 emoji por linha
- ✅ Sem travessões (-- ou ---)

### PARECER
- ✅ Estrutura completa (Resumo, Stack, Pontos Fortes, etc)
- ✅ Recomendação clara
- ✅ Offer versão curta
- ✅ Apenas português brasileiro
- ✅ ZERO emojis

## Scoring

- **10/10**: Segue todas as regras
- **9/10**: 1 violação menor (typo, formatação)
- **8/10**: 2 violações menores
- **7/10**: 1 violação maior ou 3+ menores
- **6/10**: 2 violações maiores
- **5-0**: Múltiplas falhas críticas

## Output (JSON apenas)

```json
{"passed":true,"score":10,"evaluations":[{"criterion":"regra","status":"PASS","evidence":"verificado"}],"final_verdict":"resumo"}
```

Se todas regras passarem → passed=true, score=10
Se qualquer regra crítica falhar → passed=false, score≤7
