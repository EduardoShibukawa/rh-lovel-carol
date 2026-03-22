---
name: lovel-parecer
description: "Parecer estruturado de hunting para envio à recruiter antes da entrevista.
Use para: (1) Criar resumo de perfil, (2) Estruturar experiencia relevante,
(3) Listar stack/tecnologias, (4) Avaliar fit, (5) Gerar recomendacao.
Não use para: criar boolean queries, outreach ou posts."
---

# PARECER

## INPUT

Recebe dois perfis:
- `perfil`: dados do candidato (LinkedIn, CV, etc.)
- `vaga`: requisitos da vaga

Extraia:
- `experiencia`: empresas, períodos, atuação
- `stack`: tecnologias por categoria
- `nivel`: junior/pleno/senior/lead (ver critérios abaixo)
- `fit`: alinhamento com vaga

**Critérios de senioridade:**
- Junior: 0-2 anos
- Pleno: 2-4 anos
- Senior: 4-7 anos
- Lead: 7+ anos

**Regras para perfis incompletos:**
- Se informação indisponível: usar "[N/I]" e listar no checklist
- Se experiência curta: mencionar no resumo e pontos de atenção
- Nunca inventar informações

## ESTRUTURA (obrigatória)

```
Resumo do perfil
[2-3 frases: quem é + experiência principal + contexto de mercado]

Experiência relevante
[Empresa] ([período])
[Atuação com detalhes técnicos]

Stack / Tecnologias
[Categoria]: [itens]
[Categoria]: [itens]

Pontos fortes
- [Ponto específico]
- [Ponto específico]
- [Ponto específico]

Pontos de atenção
- [Ponto específico]
- [Ponto específico]

Recomendação
[OK/NOK] Recomendo [avançar/não avançar] para entrevista, para validar:
- [Ponto específico]
- [Ponto específico]
```

## REGRAS

- Apenas português brasileiro
- Informações específicas (não genéricas)
- Não inventar informações
- Máximo 1 página
- Incluir contexto de empresa/setor quando disponível
- ZERO emojis
- Pontos fortes = competências verificáveis
- Pontos de atenção = riscos reais

## EXEMPLOS

### Exemplo 1: Perfil Forte
**Input:** "Parecer para Rafael - Go Sr 8 anos - Nubank - vaga: Go Senior R$15k-22k"

```
Resumo do perfil
Rafael é desenvolvedor Go Senior com 8 anos de experiência em backend. Atua com foco em microsserviços, 
arquitetura distribuída e sistemas de alta disponibilidade. Atualmente na Nubank, fintech de grande porte.

Experiência relevante
Nubank (2022 - atual)
Backend Engineer Sr focado em microsserviços de pagamentos. Atua com Go, gRPC, Kafka e AWS processando 
milhões de transações diárias.

Stack / Tecnologias
Linguagens: Go, Python
Frameworks: gRPC, Gin, Echo
Cloud: AWS (EKS, Lambda, SQS, RDS)
Mensageria: Kafka, RabbitMQ
Databases: PostgreSQL, Cassandra

Pontos fortes
- Longa experiência com Go (8 anos)
- Atuação em fintech de grande porte
- Experiência com arquitetura distribuída

Pontos de atenção
- Salary pode estar acima da faixa
- Disponibilidade para modelo híbrido

Recomendação
[OK] Recomendo avançar para entrevista técnica, para validar:
- Detalhes de arquitetura de pagamentos
- Experiência com escalabilidade
- Disponibilidade para trabalho híbrido
```

### Exemplo 2: Perfil Borderline
**Input:** "Parecer para Ana - Python 3 anos - Startup - vaga: Python Senior"

```
Resumo do perfil
Ana é desenvolvedora Python com 3 anos de experiência em backend. Atua com Django e APIs REST em startup 
de fintech. Expertise com sistemas de menor complexidade.

Experiência relevante
StartupXYZ (2022 - atual)
Backend Developer com foco em APIs REST e Django. Atuou em sistema de pagamentos simplificado.

Stack / Tecnologias
Linguagens: Python, JavaScript
Frameworks: Django, FastAPI, Flask
Databases: PostgreSQL, Redis

Pontos fortes
- Conhecimento em Python e frameworks web
- Experiência com APIs REST
- Atuação em fintech

Pontos de atenção
- Tempo de experiência (3 anos) abaixo do esperado para Senior
- Sistemas de menor complexidade
- Falta experiência com microsserviços

Recomendação
[NOK] Não recomendo para Senior. Considerar para Pleno, para validar:
- Complexidade dos sistemas anteriores
- Autonomia técnica em projetos maiores
```

### Exemplo 3: Perfil Incompleto
**Input:** "Parecer para Carlos - LinkedIn com info limitada"

```
Resumo do perfil
Carlos possui experiência com Java e desenvolvimento backend. Perfil com informações limitadas no LinkedIn.

Experiência relevante
[N/I] (informações não disponíveis no perfil)

Stack / Tecnologias
[N/I]: Java, SQL

Pontos fortes
[N/I]

Pontos de atenção
- Informações limitadas no perfil
- Não foi possível validar experiência
- Perfil pode não estar atualizado

Recomendação
[N/I] Informações insuficientes para avaliar. Necessário:
- Solicitar CV completo
- Agendar briefing de 15 min
```

## CHECKLIST

- [ ] Resumo com contexto de mercado
- [ ] Experiência com detalhes técnicos
- [ ] Stack categorizada
- [ ] 3 pontos fortes específicos
- [ ] 2 pontos de atenção realistas
- [ ] Recomendação clara com próximos passos
