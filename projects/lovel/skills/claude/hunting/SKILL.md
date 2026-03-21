---
name: lovel-hunting
description: "Boolean queries, X-Ray search, sourcing ativo e estratégia de recruiting. 
Use para: (1) Criar boolean strings para LinkedIn Recruiter, (2) Buscar perfis invisíveis 
(text-poor profiles), (3) Desenvolver sourcing strategy com ICP, (4) Executar X-Ray via Google.
Não use para: escrever outreach, criar posts, analisar CVs."
---

# HUNTING

REGRAS OBRIGATORIAS:
1. ZERO EMOJIS - Nenhum emoji na resposta
2. MINIMO 5 SINONIMOS - No minimo 5 sinonimos para cada termo tecnico principal
3. X-RAY - Incluir "site:linkedin.com/in" na resposta
4. NOT - Excluir: junior OR jr OR trainee OR estagio OR estágio OR aprendiz OR estágiario
5. SALARY - Formato: "R$ Xk – R$ Yk" (com en-dash, nao hyphen)

OUTPUT (seguir ordem EXATA):

## ICP
[Resumo da tese de busca - foco em impacto e resultados]

## Salary
R$ Xk – R$ Yk

## Query
(sin1 OR sin2 OR sin3 OR sin4 OR sin5 OR sin6 OR sin7 OR sin8)
AND (sin1 OR sin2 OR sin3 OR sin4 OR sin5 OR sin6 OR sin7 OR sin8)
AND ("Cidade" OR "Cidade, UF" OR "Regiao" OR "Regiao Metropolitana")
NOT (junior OR jr OR trainee OR estagio OR estágio OR aprendiz OR estágiario)

## X-Ray
site:linkedin.com/in "termo1" "termo2" "termo3" "termo4" "cidade"

## NOT
NOT (junior OR jr OR trainee OR estagio OR estágio OR aprendiz OR estágiario)

EXEMPLO COMPLETO:

## ICP
Senior Go developer com experiencia em Kubernetes, AWS e arquiteturas cloud-native para trabalho remoto no Brasil.

## Salary
R$ 15k – R$ 22k

## Query
("Go" OR "Golang" OR "Go developer" OR "Gopher" OR "Go-lang" OR "Go backend" OR "Go software" OR "Go engineer")
AND ("Kubernetes" OR "K8s" OR "K8" OR "Kube" OR "EKS" OR "container orchestrator" OR "container orchestration" OR "Docker")
AND ("AWS" OR "Amazon Web Services" OR "AWS cloud" OR "Amazon AWS" OR "AWS EC2" OR "AWS Lambda" OR "AWS EKS" OR "cloud AWS")
AND ("Remoto" OR "Remote" OR "Work from home" OR "Remote work" OR "Home office" OR "Anywhere" OR "Brasil" OR "Brazil")
NOT (junior OR jr OR trainee OR estagio OR estágio OR aprendiz OR estágiario)

## X-Ray
site:linkedin.com/in "Go" "Golang" "Kubernetes" "AWS" "Remote"

## NOT
NOT (junior OR jr OR trainee OR estagio OR estágio OR aprendiz OR estágiario)

CHECKLIST:
- [ ] Zero emojis
- [ ] Minimo 5 sinonimos para CADA termo
- [ ] X-Ray com site:linkedin.com/in
- [ ] NOT exclusions completas
- [ ] Salary R$ Xk – R$ Yk (en-dash)
