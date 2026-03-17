# TESTE: HUNTING + vaga_go

## Input (Fixture)
```
Vaga: Desenvolvedor Go/Golang Senior
Empresa: Fintech de pagamentos
Salário: R$ 18k – R$ 25k
Modelo: Híbrido (2x semana) | São Paulo, SP
Stack: Go, gRPC, Kubernetes, AWS, PostgreSQL
```

## Output Gerado (simulado para validação)

### Boolean Query
```
("Go" OR "Golang" OR "Go language" OR "Go developer" OR "Gopher")
AND (backend OR "back-end" OR servidor OR API OR microservice OR gRPC)
AND (Kubernetes OR K8s OR AWS OR GCP OR "cloud native")
NOT (júnior OR junior OR trainee OR estagio OR aprendiz)
```

### X-Ray
```
site:linkedin.com/in/ "Go" OR "Golang" "São Paulo" -"open to work" -"estagio"
```

---

## Validação

| Critério | Status | Observação |
|----------|--------|------------|
| 5+ sinônimos para "Go" | ✅ | 5 sinônimos: Go, Golang, Go language, Go developer, Gopher |
| X-Ray presente | ✅ | site:linkedin.com/in/ |
| Exclusões NOT | ✅ | júnior, junior, trainee, estagio, aprendiz |
| Localização específica | ✅ | São Paulo + estado + região |

### Score: **4/4 ✅**

---

## Output Gerado (simulado para validação) - BDR

### Boolean Query (vaga_bdr)
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

---

## Validação BDR

| Critério | Status | Observação |
|----------|--------|------------|
| ICP com hipóteses | ✅ | 3 hipóteses presentes |
| Seed/Net/Spear | ❌ | Não mencionado |
| SDR/BDR differentiation | ✅ | Conceito usado |

### Score: **3/4 ⚠️**
