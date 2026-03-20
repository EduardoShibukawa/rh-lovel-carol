---
name: lovel-hunting
description: "Boolean queries, X-Ray search, sourcing ativo e estratégia de recruiting. 
Use para: (1) Criar boolean strings para LinkedIn Recruiter, (2) Buscar perfis invisíveis 
(text-poor profiles), (3) Desenvolver sourcing strategy com ICP, (4) Executar X-Ray via Google.
Não use para: escrever outreach, criar posts, analisar CVs."
---

# HUNTING

REGRAS OBRIGATÓRIAS:
1. ZERO EMOJIS - Nenhum emoji na resposta
2. 5+ SINÔNIMOS - Exatamente 5 ou mais sinônimos para cada termo técnico
3. X-RAY - Incluir "site:linkedin.com/in" na resposta
4. NOT - Excluir: junior OR júnior OR trainee OR estagio OR estágio OR aprendiz
5. SALARY - Formato: "R$ Xk – R$ Yk" (com en-dash, não hyphen)

OUTPUT (seguir ordem EXATA):

## ICP
[Resumo da tese de busca]

## Salary
R$ Xk – R$ Yk

## Query
(sin1 OR sin2 OR sin3 OR sin4 OR sin5 OR sin6)
AND (sin1 OR sin2 OR sin3 OR sin4 OR sin5 OR sin6)
AND ("Cidade" OR "Cidade, UF")
NOT (júnior OR junior OR trainee OR estagio OR estágio OR aprendiz)

## X-Ray
site:linkedin.com/in "termo1" "termo2" "cidade"

## NOT
NOT (júnior OR junior OR trainee OR estagio OR estágio OR aprendiz)

EXEMPLO COMPLETO:

## ICP
Senior Go developer para microservices cloud-native.

## Salary
R$ 15k – R$ 22k

## Query
("Go" OR "Golang" OR "Go developer" OR "Gopher" OR "Go-lang" OR "Go backend" OR "Go software")
AND (Kubernetes OR K8s OR AWS OR GCP OR Docker OR Azure OR container OR "cloud native")
AND ("São Paulo" OR "São Paulo, SP" OR "SP" OR "Região Sudeste")
NOT (júnior OR junior OR trainee OR estagio OR estágio OR aprendiz)

## X-Ray
site:linkedin.com/in "Go" "Golang" "Kubernetes" "São Paulo"

## NOT
NOT (júnior OR junior OR trainee OR estagio OR estágio OR aprendiz)

CHECKLIST:
- [ ] Zero emojis
- [ ] 5+ sinônimos para CADA termo
- [ ] X-Ray com site:linkedin.com/in
- [ ] NOT exclusions completas
- [ ] Salary R$ Xk – R$ Yk (en-dash, não hyphen)
