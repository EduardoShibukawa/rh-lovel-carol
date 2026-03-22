---
name: lovel-post
description: "LinkedIn Posts com impacto de 90 dias, transparência salarial e DNA Lovel. 
Use para: (1) Criar posts para vagas tech, (2) Escrever hooks baseados em resultados de 90 dias, 
(3) Estruturar posts com salary explícito, (4) Formatar para LinkedIn.
Não use para: escrever outreach, criar boolean queries, analisar CVs."
---

# POST - LinkedIn Posts & Hooks de Impacto

## INPUT

Extraia do prompt:
- `title`: titulo da vaga
- `salary`: faixa salarial (ex: R$ 15k-22k)
- `model`: remoto/híbrido/presencial
- `city`: cidade
- `stack`: tecnologias principais
- `metrics`: metricas de impacto se disponivel

**Regras para campos ausentes:**
- Se `salary` ausente: estimar baseado no nivel (Pleno: R$ 8k-14k, Senior: R$ 15k-22k, Lead: R$ 20k-30k)
- Se `metrics` ausente: focar em "desafio de dominio" (ex: "trabalhar com sistemas de pagamentos")
- Se `model` ausente: usar "Remoto"
- Se `city` ausente: omitir ou usar "Brasil"

## HOOKS

Hook é a primeira linha. Deve mostrar impacto em 90 dias.

### Tipo 1: Métricas Técnicas
```
Tornar a API 3x mais rápida em 90 dias
Escalar de 10k para 100k usuários em 90 dias
Reduzir downtime de 5% para 0.1% em 90 dias
Implementar CI/CD completo em 90 dias
```

### Tipo 2: Desafio de Domínio
```
Trabalhar com sistemas de pagamentos em 90 dias
Liderar migração para microservices em 90 dias
Estruturar área de dados em 90 dias
Construir plataforma de fintech do zero em 90 dias
```

### Tipo 3: Oportunidade de Impacto
```
Impactar milhões de usuários em 90 dias
Resolver dívidas técnicas de sistema crítico em 90 dias
Construir time de elite em 90 dias
```

### Hooks RUIM (NAO USAR)
```
Senior Backend Engineer (cargo, não impacto)
Fazer parte de um time incrível (vago)
Liderar decisões técnicas (vago)
```

## ESTRUTURA

```
[Hook com impacto em 90 dias]

R$ Xk – R$ Yk | [CLT/PJ] | [Senior/Pleno]
[Modelo] | [Cidade]
[Stack principal]
app.lovel.dev/vaga?invite=caroline.lima798
```

**Nota:** Use hifen curto (-) para separadores, en-dash (–) apenas em faixas salariais.

## EXEMPLOS

### Exemplo 1: Backend Senior
**Input:** "Post para Dev Go Sr - R$18k-25k - CLT - São Paulo - Go, AWS, Kubernetes"

```
Tornar a API 3x mais rápida em 90 dias

R$ 18k – R$ 25k | CLT | Sênior
Híbrido | São Paulo, SP
Go, AWS, Kubernetes
app.lovel.dev/vaga?invite=caroline.lima798
```

### Exemplo 2: DevOps (sem metrics)
**Input:** "Post para DevOps - R$12k-18k - Remoto - AWS, Terraform"

```
Construir infraestrutura como código do zero em 90 dias

R$ 12k – R$ 18k | PJ | Pleno
Remoto | Brasil
AWS, Terraform, Kubernetes
app.lovel.dev/vaga?invite=caroline.lima798
```

### Exemplo 3: Frontend
**Input:** "Post para React Sr - R$14k-20k - Remoto - React, TypeScript"

```
Melhorar performance de web app para 100/100 Lighthouse em 90 dias

R$ 14k – R$ 20k | CLT | Sênior
Remoto | Brasil
React, TypeScript, Next.js
app.lovel.dev/vaga?invite=caroline.lima798
```

### Exemplo 4: Data Engineer
**Input:** "Post para Data Engineer - R$16k-22k - Hibrido SP - Python, Spark"

```
Construir pipeline de dados que processa GBs por dia em 90 dias

R$ 16k – R$ 22k | CLT | Sênior
Híbrido | São Paulo, SP
Python, Spark, Airflow
app.lovel.dev/vaga?invite=caroline.lima798
```

## CHECKLIST

- Hook contem "90 dias" ou indica impacto claro
- Salary com en-dash: R$ Xk – R$ Yk
- Invite: caroline.lima798
- Zero em-dash (—)
- Zero separadores (---, ===)
- Modelo e cidade presente
