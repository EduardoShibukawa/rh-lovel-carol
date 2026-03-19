---
name: lovel-parecer
description: "Parecer estruturado de hunting para envio à recruiter antes da entrevista.
Use para: (1) Criar resumo de perfil de candidato, (2) Estruturar experiência relevante,
(3) Listar stack/tecnologias, (4) Avaliar fit, (5) Gerar recomendação.
Não use para: criar boolean queries, outreach ou posts."
---

# PARECER - Relatório de Hunting para Recruiter

## Overview

Skill para criar parecer estruturado de hunting que facilita a triagem rápida do time de recrutamento. O parecer é enviado à recruiter antes do agendamento da entrevista.

## Autoridades Aplicadas

- **Lovel**: Transparência, tom profissional, estrutura clara
- **Lou Adler**: Foco em resultados e impacto (não apenas skills)

## Workflow

### Passo 1: coletar Informações do Perfil
Coletar do perfil/currículo:
- Nome completo
- Cargo atual e empresa
- Tempo de experiência
- Stack técnica
- Projetos relevantes
- Histórico profissional

### Passo 2: Estruturar Resumo do Perfil
1-2 parágrafos com:
- Cargo atual e foco principal
- Experiência relevante
- Setor atual (se relevante)

### Passo 3: Listar Experiência Relevante
Para cada experiência (máx 3):
- Empresa e período
- Atuação principal
- Tecnologias/softwares usados

### Passo 4: Compilar Stack/Tecnologias
Agrupar por categoria:
- Linguagens
- Frameworks/Bibliotecas
- Cloud/Infra
- Metodologias
- Banco de dados

### Passo 5: Avaliar Pontos Fortes
Listar 3-4 pontos positivos:
- Experiência técnica relevante
- Domínio de tecnologias demandadas
- Setor alinhado
- Metodologias ágeis

### Passo 6: Pontos de Atenção
Listar 2-3 pontos de atenção:
- Tempo de experiência
- Gaps de tecnologias
- Questões de disponibilidade
- Fit de senioridade

### Passo 7: Avaliação de Fit
Avaliação textual do match com a vaga

### Passo 8: Recomendação
Estrutura:
- ✔ ou ✘
- Recommendação de avançar ou não
- Pontos específicos para validar na entrevista

### Passo 9: Offer Bônus
"Oferecer versão curta (3-4 linhas) para ATS/Slack"

---

## Estrutura do Parecer

```
Parecer do Hunter | [Nome do Candidato] | [Cargo]

Resumo do perfil
[Resumo de 1-2 parágrafos com experiência relevante e foco]

Experiência relevante
[Empresa] ([período])
[Atuação com detalhes técnicos]

Stack / Tecnologias
- [Categoria]: [itens]
- [Categoria]: [itens]

Pontos fortes
- [Ponto 1]
- [Ponto 2]
- [Ponto 3]

Pontos de atenção
- [Ponto 1]
- [Ponto 2]

Avaliação do fit (visão de hunting)
[Avaliação textual]

Recomendação
✔ Recomendo [avançar/não avançar] para entrevista, principalmente para validar:
- [Ponto 1]
- [Ponto 2]

[Offer bônus]
```

---

## Examples

### ✅ BOM - Parecer Completo
```
Parecer do Hunter | Levi Alves | QA Engineer / SDET

Resumo do perfil
Levi atua como QA Engineer com foco em automação de testes, com experiência em testes 
manuais e automatizados para API e UI, utilizando principalmente C#, Playwright, Selenium 
e ferramentas de testes de API. Atualmente está na Zitec atuação em projeto para banco digital.

Experiência relevante

Zitec (2025 – atual)
QA focado em automação de testes para cliente do setor bancário digital. Atua com C#, 
Playwright, NUnit, Postman e HTTPClient, além de integração com esteiras de CI.

E2E Coders (2022 – 2025)
Experiência anterior como Analista de Testes, consolidando base em testes manuais e 
automação.

Stack / Ferramentas
Automação: Playwright, Selenium, Cypress
Linguagens: Java, C#, JavaScript
Testes de API: Postman, Rest-Assured
Metodologias: BDD, Cucumber, Gherkin
CI/CD: Jenkins, GitHub Actions, Azure DevOps

Pontos fortes
- Experiência prática em automação de testes de API e UI
- Vivência em ambiente ágil (Scrum/Kanban)
- Atuação em projeto de banco digital
- Conhecimento em integração de testes em pipelines CI/CD

Pontos de atenção
- Tempo de experiência total ainda relativamente curto (cerca de 3 anos)
- Formação em Engenharia de Software ainda em andamento
- Senioridade tende mais para QA Pleno inicial

Avaliação do fit
Perfil interessante para posições de QA Automation / SDET nível Pleno, principalmente 
em ambientes que utilizem Playwright, Selenium ou testes de API.

Recomendação
✔ Recomendo avançar para entrevista técnica inicial, para validar principalmente:
- Profundidade em framework de automação
- Estruturação de testes e arquitetura de testes
- Experiência real com CI/CD e pipelines

Se quiser, também posso te montar uma versão mais curta (3-4 linhas) para ATS ou Slack. 🚀
```

### ❌ RUIM - Parecer Genérico
```
Parecer do Hunter | João Silva | Dev

Resumo
João é um desenvolvedor bom, tem experiência com programação.

Pontos fortes
- É competente
- Conhece várias tecnologias

Pontos de atenção
- Não sei se serve

Recomendação
✔ Pode chamar
```
**Problemas:**
- Sem informações específicas de stack
- Sem períodos de experiência
- Avaliação vaga
- Não menciona empresa atual
- Linguagem informal demais

---

## Limitations

- **PROIBIDO**: Usar informações não presentes no perfil
- **PROIBIDO**: Inventar tecnologias ou experiências
- **PROIBIDO**: Usar palavras em outros idiomas (russo, chinês, japonês, coreano, etc)
- **PROIBIDO**: Usar palavras em inglês fora de contexto técnico (como nomes de tecnologias)
- **PROIBIDO**: Tornar o texto muito longo (máx 1 página)
- **SEMPRE**: Usar apenas português brasileiro
- **SEMPRE**: Incluir offer de versão curta no final
- **SEMPRE**: Ser transparente sobre senioridade

## Validation

- [ ] Resumo com experiência relevante?
- [ ] Stack completa e categorizada?
- [ ] Pontos fortes específicos?
- [ ] Pontos de atenção realistas?
- [ ] Recomendação com próximos passos?
- [ ] Offer de versão curta presente?
- [ ] Texto apenas em português brasileiro?
