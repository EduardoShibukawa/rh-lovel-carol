# Fixture: Vaga BDR (Comercial)

**Formato:** Briefing Individual  
**Skill Alvo:** outreach, hunting

## Entrada

```
Cliente: Berry Consultoria
Vagas: 1 vaga de BDR Pleno (Outbound).
Stack: MeTime, CRM interno, ferramentas de extração de dados da Receita Federal.
Salário: R$ 3.500,00 fixo + Comissão (podendo chegar a R$ 4.500,00 a R$ 5.000,00 mensais).
Modelo: PJ, 100% Presencial em Curitiba/PR (Segunda a Sexta, das 08h às 18h).
Cultura: Operação nova, em constante desenvolvimento e otimização de processos. 
```

## Expected Output (OUTREACH)

### M1 (Máx 300 chars)
```
Oi [Nome]! Sou Carol, parceira da Lovel. Vi seu perfil e acredito que possa 
lhe interessar uma oportunidade de BDR em consultoria de Curitiba. 
Está avaliando novas oportunidades?
```

### M2
```
Perfeito! Vou te compartilhar mais detalhes 😊

Empresa: Berry Consultoria
Cargo: BDR Pleno | Pleno
Atuação: Prospecção outbound, cold calling, qualificação de leads
Modelo: PJ | Curitiba, PR
Remuneração: R$ 3.5k – R$ 5k (fixo + comissão)
Diferencial: Operação nova com crescimento rápido

Faz sentido?

🔗 app.lovel.dev/?invite=caroline.lima798
```

## Expected Output (HUNTING)

### Boolean Query (Aaron Ross ICP)
```
("BDR" OR "SDR" OR "Sales Development" OR "Pré-vendas" OR "Executivo de Contas" OR "Consultor Comercial")
AND (outbound OR prospecção OR "cold call" OR "lead generation" OR pipeline)
AND ("Curitiba" OR "Curitiba, PR" OR "Região Metropolitana de Curitiba")
NOT (estágio OR trainee OR aprendiz OR júnior OR junior)
```

### ICP Hipóteses (Aaron Ross)
- Targeting: Empresas de consultoria, SaaS B2B
- Need: Geração de pipeline, prospecção ativa
- Solution: Challenger sale, VALUE selling
