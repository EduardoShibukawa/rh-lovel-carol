# Fixture: Vaga Go (Backend)

**Formato:** Briefing Técnico  
**Skill Alvo:** hunting, post

## Entrada

```
Vaga: Desenvolvedor Go/Golang Senior
Empresa: Fintech de pagamentos
Salário: R$ 18k – R$ 25k
Modelo: Híbrido (2x semana) | São Paulo, SP
Stack: Go, gRPC, Kubernetes, AWS, PostgreSQL
Impacto: Sistemas que processam milhões de transações/dia
```

## Expected Output (HUNTING)

### Boolean Query (5+ sinônimos - Glen Cathey)
```
("Go" OR "Golang" OR "Go language" OR "Go developer" OR "Gopher")
AND (backend OR "back-end" OR servidor OR API OR microservice OR gRPC)
AND (Kubernetes OR K8s OR AWS OR GCP OR "cloud native")
NOT (júnior OR junior OR trainee OR estagio OR aprendiz)
```

### X-Ray (Glen Cathey)
```
site:linkedin.com/in/ "Go" OR "Golang" "São Paulo" -"open to work" -"estagio"
```

### Sourcing Strategy
- Target Companies: Nubank, Creditas, PagSeguro, Stone, Mercado Pago
- Insight: Buscar em comunidades Go Brasil, Meetups, GitHub

## Expected Output (POST)

### Hook (Lou Adler - 90 dias)
```
🚀 Tornar sistemas de pagamento 3x mais rápidos em 90 dias
💰 R$ 18k – R$ 25k | CLT | Sênior
📍 Híbrido | São Paulo, SP
🛠️ Go, gRPC, Kubernetes, AWS
🔗 app.lovel.dev/?invite=caroline.lima798
```
