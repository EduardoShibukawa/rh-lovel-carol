---
name: hunting
description: "Boolean queries, X-Ray search, sourcing ativo e estratégia de recruiting. 
Use para: (1) Criar boolean strings para LinkedIn Recruiter, (2) Buscar perfis invisíveis 
(text-poor profiles), (3) Desenvolver sourcing strategy com ICP, (4) Executar X-Ray via Google.
Não use para: escrever outreach, criar posts, analisar CVs."
---

# HUNTING - Boolean Queries & Sourcing Strategy

## Overview

Skill para criar boolean queries de alta qualidade e sourcing strategy, seguindo os princípios de Glen Cathey (Boolean Black Belt), Aaron Ross (Predictable Revenue) e Gergely Orosz (Pragmatic Engineer).

## Autoridades Aplicadas

- **Glen Cathey**: 5+ sinônimos, X-Ray, text-poor profiles, dark matter, iterative search
- **Aaron Ross**: ICP com hipóteses testáveis, Seed/Net/Spear, SDR/BDR
- **Gergely Orosz**: Senioridade = autonomia/impacto (não tempo de casa)
- **Lovel**: SLA 10 dias, velocidade no sourcing

## Workflow

### Passo 1: Validar ICP
Se dados incompletos, apresentar opções:
- Senioridade: junior/pleno/senior?
- Setor: SaaS/consultoria/agência?
- Tipo: cold/ABM/inbound?
- Localização: cidade ou região?

### Passo 2: Expandir Sinônimos (Mínimo 5)
Para cada termo técnico:
- Termo original
- 5 sinônimos ou variações de cargo
- Alternative titles do mercado

### Passo 3: Construir Boolean String
Estrutura:
```
(termo1 OR termo2 OR termo3...) 
AND (conceito1 OR conceito2...) 
AND (localização)
NOT (estagio OR trainee OR aprendiz OR júnior OR junior)
```

### Passo 4: X-Ray Search (Google Bypass)
```
site:linkedin.com/in/ "termo" "Brasil" -"open to work"
```

### Passo 5: Sourcing Strategy
- Target Companies: onde o talento já está pronto
- Insight: onde caçar além do LinkedIn

## Examples

### ✅ BOM - Boolean Query para Go/Golang Backend
```
("Go" OR "Golang" OR "Go language" OR "Go developer" OR "Gopher")
AND (backend OR "back-end" OR servidor OR API OR microservice)
AND (Kubernetes OR K8s OR AWS OR GCP OR Azure OR "cloud native")
NOT (júnior OR junior OR trainee OR estagio OR aprendiz)
```

### ✅ BOM - Boolean Query para SDR/BDR (Aaron Ross ICP)
```
("SDR" OR "BDR" OR "Sales Development" OR "Pré-vendas" OR "Executivo de Contas" OR "Consultor Comercial")
AND (outbound OR prospecção OR "cold call" OR "lead generation" OR pipeline OR "prospecting")
AND ("Curitiba" OR "Curitiba, PR" OR "Região Metropolitana de Curitiba")
NOT (estágio OR trainee OR aprendiz OR júnior OR junior)
```

### ❌ RUIM - Query Básica (Sem sinônimos suficientes)
```
"Go Developer" "Brasil"
```

### ❌ RUIM - Query Sem Exclusões
```
("SDR" OR "BDR") AND ("Curitiba")
```

## Limitations

- **PROIBIDO**: Mencionar ferramentas específicas (MeTime, Pipedrive) - são critérios de triagem
- **PROIBIDO**: Usar apenas estado (gera muito ruído) - usar cidade + região
- **NUNCA**: Inventar dados de impacto que não existam na vaga

## Validation

- [ ] Mínimo 5 sinônimos por termo técnico?
- [ ] X-Ray search incluída (site:linkedin.com/in)?
- [ ] Exclusões (NOT) para júnior/estágio?
- [ ] Localização específica (cidade + estado + região)?
- [ ] ICP estruturado com hipóteses (para vagas comerciais)?
- [ ] Referência a text-poor profiles (candidatos invisíveis)?
