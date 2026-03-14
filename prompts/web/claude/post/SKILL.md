---
name: lovel-post
description: "LinkedIn Posts com impacto de 90 dias, transparência salarial e DNA Lovel. 
Use para: (1) Criar posts para vagas tech, (2) Escrever hooks baseados em resultados, 
(3) Estruturar posts com salary explícito, (4) Formatar para LinkedIn Algo.
Não use para: escrever outreach, criar boolean queries, analisar CVs."
---

# POST - LinkedIn Posts & Hooks de Impacto

## Overview

Skill para criar LinkedIn Posts seguindo Lou Adler (Performance-based Hiring - impacto de 90 dias), com transparência salarial e tom humano da Lovel.

## Autoridades Aplicadas

- **Lou Adler**: Impacto de 90 dias, outcome > skills, career growth (30% mais desafio)
- **Gergely Orosz**: Desafios técnicos reais, terminologia correta
- **Lovel**: Transparência radical (salário sempre explícito), invite parameter

## Workflow

### Passo 1: Hook de Impacto (90 Dias)
O título deve focar no **resultado mensurável** em 90 dias, não no nome do cargo.

**Com dado de impacto (usar dados reais da vaga):**
- BOM: "Tornar a API 3x mais rápida em 90 dias"
- BOM: "Escalar de 10k para 100k usuários"
- BOM: "Reduzir downtime de 5% para 0.1%"

**Sem dado de impacto (usar contextualização genérica técnica):**
- BOM: "Trabalhar em sistemas de alto tráfego que processam milhões de transações"
- BOM: "Estruturar área de QA em plataforma utilizada por milhares de usuários"
- RUIM: "Liderar decisões técnicas e orientar um time"

### Passo 2: Contexto
Se a entrada não tiver setor definido, usar placeholder:
- fintech, healthtech, SaaS, etc.

### Passo 3: Estrutura do Post
```
[Hook = resultado 90 dias]
[Contexto: setor ou produto]

🚀 [Desafio real | 1 frase direta com resultado mensurável]
💰 [Faixa salarial normalizada: R$ Xk – R$ Yk] | [CLT ou PJ] | [Sênior/Pleno/etc]
📍 [Modelo de trabalho | Cidade/UF]
🛠️ [Stack principal ou ferramentas]
🔗 [link app.lovel.dev com invite da Carol]
```

### Passo 4: Validação Salary
**REGRA CRÍTICA**: Toda vaga deve ter **faixa**, não valor único.

Se entrada tiver apenas um valor:
- **Opção 1**: Calcular faixa automática (variação ±20%)
  - Ex: R$ 10k → R$ 8k – R$ 12k
- **Opção 2**: Inferir faixa por nível
  - Pleno: valor – 20% a valor
  - Sênior: valor a valor + 30%
- **Opção 3**: Perguntar se nenhuma opção for clara

### Passo 5: Múltiplas Vagas (Máx 4 por post)
- Variar hooks (não usar sempre "🚀 [verbo]...")
- Até 4 vagas é a recomendação (LinkedIn Algo - dwell time)
- Se >4 vagas, sugerir dividir em múltiplos posts

## Examples

### ✅ BOM - Hook com Impacto (Lou Adler)
```
🚀 Tornar a API 3x mais rápida em 90 dias

💰 R$ 18k – R$ 25k | CLT | Sênior
📍 Híbrido | São Paulo, SP
🛠️ Go, AWS, Kubernetes
🔗 app.lovel.dev/vagas/?invite=caroline.lima798
```

### ✅ BOM - Hook sem Dado Específico
```
🚀 Trabalhar em sistemas de alto tráfego que processam milhões de transações

💰 R$ 15k – R$ 22k | CLT | Pleno/Sênior
📍 Remoto | Brasil
🛠️ Java, Spring Boot, PostgreSQL
🔗 app.lovel.dev/vagas/?invite=caroline.lima798
```

### ❌ RUIM - Hook Genérico (SEM IMPACTO)
```
🚀 Fazer parte de um time incrível e colaborativo

💰 R$ 10k – R$ 15k | CLT | Sênior
📍 Presencial | Curitiba, PR
🛠️ .NET, C#, SQL Server
```

### ❌ RUIM - Cargo como Hook
```
🚀 Senior Backend Engineer

💰 R$ 12k – R$ 18k | CLT
📍 Híbrido | São Paulo
🔗 app.lovel.dev
```

## Limitations

- **PROIBIDO**: Usar cargo como hook (ex: "Senior Backend Engineer")
- **PROIBIDO**: Usar separadores (---, ===, ___) ou rótulos (POST 1, VAGA 1)
- **PROIBIDO**: Usar mais de 1 emoji por linha
- **PROIBIDO**: Travessões (—)
- **SEMPRE**: Faixa salarial explícita (nunca "a combinar")
- **SEMPRE**: Link com invite=caroline.lima798

## Validation

- [ ] Hook foca em impacto de 90 dias (outcome, não cargo)?
- [ ] Salary em faixa explícita?
- [ ] Máximo 4 vagas por post?
- [ ] Emoji máximo 1 por linha?
- [ ] Link com invite parameter?
- [ ] Sem separadores ou travessões?
