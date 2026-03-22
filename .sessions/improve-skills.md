# Melhorar Skills para 9.5+ na Avaliação

## Contexto

Use `/skill-tester` para melhorar as skills até 9.5+.

## Scores Atuais

| Skill | Score | Issues |
|-------|-------|--------|
| hunting | 8.8 | Falta ICP guidance, salary range |
| outreach | 8.6 | Personalização genérica, invite não claro |
| post | 8.8 | Hífen vs en-dash, hooks por setor |
| parecer | 8.8 | Perfis incompletos, critérios fit |

## Fluxo

1. Rodar `python skills/skill-tester/scripts/assess.py --project lovel --skill <skill>`
2. Identificar issues
3. Melhorar SKILL.md
4. Rerodar assess.py
5. Repetir até 9.5+

## Issues Específicos a Corrigir

### Hunting (8.8 → 9.5+)
- Adicionar seção "Perguntas iniciais" para coletar info da vaga
- Incluir referência sobre como definir salary range
- Adicionar 2-3 exemplos com stacks diferentes

### Outreach (8.6 → 9.5+)
- Adicionar exemplo de personalização com info do candidato
- Incluir explicitamente invite=no link: `🔗 https://lovel.com.br/vaga?invite=caroline.lima798`

### Post (8.8 → 9.5+)
- Adicionar exemplo visual de hífen (-) vs en-dash (–)
- Incluir mais exemplos de hooks por setor (fintech, healthtech, SaaS)

### Parecer (8.8 → 9.5+)
- Adicionar guideline para perfis com info limitadas
- Incluir critérios de senioridade (Jr 0-2, Pl 2-4, Sr 4-7)

## Scripts Úteis

```bash
# Avaliar skill específica
python skills/skill-tester/scripts/assess.py --project lovel --skill hunting

# Validar fixtures CUE
python skills/skill-tester/scripts/validate.py --project lovel

# Todas as skills
python skills/skill-tester/scripts/assess.py --project lovel
python skills/skill-tester/scripts/validate.py --project lovel
```
