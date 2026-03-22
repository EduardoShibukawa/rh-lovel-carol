---
name: lovel-hunting
description: "Boolean queries, X-Ray search, sourcing ativo e estratégia de recruiting. 
Use para: (1) Criar boolean strings para LinkedIn Recruiter, (2) Buscar perfis invisíveis 
(text-poor profiles), (3) Desenvolver sourcing strategy com ICP, (4) Executar X-Ray via Google.
Não use para: escrever outreach, criar posts, analisar CVs."
---

# HUNTING

## INPUT

Extraia do prompt os campos:
- `tech`: tecnologias principais (ex: Go, Kubernetes)
- `level`: nivel desejado (ex: Senior, Pleno)
- `salary`: faixa salarial se disponivel (ex: R$ 15k-22k)
- `location`: cidade, estado ou "Remoto" (default: Brasil)

**Regras para campos ausentes:**
- Se `salary` ausente: estimar baseado no `level` (Pleno: R$ 8k-12k, Senior: R$ 15k-22k, Lead: R$ 20k-30k)
- Se `location` ausente: usar "Remoto" + "Brasil"
- Se `tech` ambiguo: adicionar sinônimos óbvios (ex: "Java" → "Java", "JVM", "Spring", "Spring Boot")

## Regras

1. ZERO EMOJIS
2. MINIMO 5 SINONIMOS por termo técnico principal
3. Termos multi-palavra usam ASPAS DUPLAS (ex: "Amazon Web Services")
4. X-RAY inclui "site:linkedin.com/in"
5. NOT exclui: junior OR jr OR trainee OR estagio OR estágio OR aprendiz OR estágiario
6. SALARY usa en-dash: "R$ Xk – R$ Yk" (não hyphen "-")

## OUTPUT (ordem EXATA)

```
## ICP
[2-3 frases: quem procurar + impacto + contexto]

## Salary
R$ Xk – R$ Yk

## Query
(...)

## X-Ray
site:linkedin.com/in "termo1" "termo2" "termo3"

## NOT
NOT (...)
```

## EXEMPLO 1: Padrao

**Input:** "Boolean para Dev Go Sr - R$15k-22k - remoto - Go, Kubernetes, AWS"

```
## ICP
Senior Go developer com experiência em Kubernetes e AWS para trabalho remoto no Brasil.

## Salary
R$ 15k – R$ 22k

## Query
("Go" OR "Golang" OR "Go developer" OR "Gopher" OR "Go-lang" OR "Go backend" OR "Go software" OR "Go engineer")
AND ("Kubernetes" OR "K8s" OR "K8" OR "Kube" OR "EKS" OR "container orchestrator" OR "Docker")
AND ("AWS" OR "Amazon Web Services" OR "AWS cloud" OR "Amazon AWS" OR "AWS EC2" OR "AWS Lambda" OR "cloud AWS")
AND ("Remoto" OR "Remote" OR "Work from home" OR "Home office" OR "Anywhere" OR "Brasil" OR "Brazil")
NOT (junior OR jr OR trainee OR estagio OR estágio OR aprendiz OR estágiario)

## X-Ray
site:linkedin.com/in "Go" "Golang" "Kubernetes" "AWS" "Remote"

## NOT
NOT (junior OR jr OR trainee OR estagio OR estágio OR aprendiz OR estágiario)
```

## EXEMPLO 2: Multi-stack

**Input:** "Backend Python Django - Pleno - Remoto - Python, Django, PostgreSQL"

```
## ICP
Backend Engineer com Django e PostgreSQL para posicao plena remota.

## Salary
R$ 8k – R$ 14k

## Query
("Python" OR "Python developer" OR "Python backend" OR "Django" OR "Django REST" OR "Python engineer")
AND ("Django" OR "Django framework" OR "Django ORM" OR "Django REST framework")
AND ("PostgreSQL" OR "Postgres" OR "PSQL" OR "Postgre")
AND ("Remoto" OR "Remote" OR "Home office" OR "Anywhere" OR "Brasil" OR "Brazil")
NOT (junior OR jr OR trainee OR estagio OR estágio OR aprendiz OR estágiario)

## X-Ray
site:linkedin.com/in "Python" "Django" "PostgreSQL" "Remote"

## NOT
NOT (junior OR jr OR trainee OR estagio OR estágio OR aprendiz OR estágiario)
```

## EXEMPLO 3: Sem salary (estimar)

**Input:** "DevOps AWS experiencia em infraestrutura - remoto"

```
## ICP
DevOps Engineer com AWS e Terraform para trabalho remoto no Brasil.

## Salary
R$ 12k – R$ 18k

## Query
("DevOps" OR "DevOps Engineer" OR "SRE" OR "Site Reliability" OR "Cloud Engineer" OR "Infrastructure Engineer")
AND ("AWS" OR "Amazon Web Services" OR "Amazon AWS" OR "AWS cloud" OR "EC2" OR "S3" OR "Lambda" OR "cloud AWS")
AND ("Terraform" OR "Ansible" OR "Pulumi" OR "CloudFormation" OR "IaC")
AND ("Remoto" OR "Remote" OR "Home office" OR "Anywhere" OR "Brasil" OR "Brazil")
NOT (junior OR jr OR trainee OR estagio OR estágio OR aprendiz OR estágiario)

## X-Ray
site:linkedin.com/in "DevOps" "AWS" "Terraform" "Remote"

## NOT
NOT (junior OR jr OR trainee OR estagio OR estágio OR aprendiz OR estágiario)
```

## CHECKLIST

- [ ] Zero emojis
- [ ] Minimo 5 sinonimos para CADA termo
- [ ] Termos multi-palavra com aspas
- [ ] X-Ray com site:linkedin.com/in
- [ ] NOT exclusions completas
- [ ] Salary com en-dash (R$ Xk – R$ Yk)
