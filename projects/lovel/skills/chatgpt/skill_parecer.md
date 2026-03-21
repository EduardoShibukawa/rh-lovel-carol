<skill>
<name>skill_parecer</name>
<description>Parecer estruturado de hunting para envio à recruiter antes da entrevista. Use para: (1) Criar resumo de perfil, (2) Estruturar experiencia relevante, (3) Listar stack/tecnologias, (4) Avaliar fit, (5) Gerar recomendacao. Não use para: criar boolean queries, outreach ou posts.</description>

<instructions>
ESTRUTURA (OBRIGATORIA):

Resumo do perfil
[Resumo com experiencia e foco - incluir contexto de empresa/setor se disponivel]

Experiencia relevante
[Empresa] ([periodo])
[Atuacao com detalhes tecnicos e resultados]

Stack / Tecnologias
[Tecnologias por categoria]

Pontos fortes
- [Ponto 1 - especifico]
- [Ponto 2 - especifico]
- [Ponto 3 - especifico]

Pontos de atencao
- [Ponto 1 - especifico]
- [Ponto 2 - especifico]

Recomendacao
[OK/NOK] Recomendo [avancar/nao avancar] para entrevista, para validar:
- [Ponto especifico para validar]

REGRAS:
- Apenas portugues brasileiro
- Informacoes especificas (nao genericas)
- Nao inventar informacoes
- Maximo 1 pagina
- Incluir contexto de empresa/setor quando disponivel
</instructions>

<examples>
### BOM
Input: Parecer para Rafael - Dev Go Sr - Nubank - 8 anos experiencia

Output:
Resumo do perfil
Rafael e desenvolvedor Go Senior com 8 anos de experiencia em backend. Atua com foco em microservicos, arquitetura distribuida e sistemas de alta disponibilidade. Atualmente na Nubank, uma das maiores fintechs da America Latina.

Experiencia relevante
Nubank (2022 - atual)
Backend Engineer Sr focado em microservicos de pagamentos. Atua com Go, gRPC, Kafka e AWS em ambiente de alta disponibilidade processando milhoes de transacoes diarias.

Stack / Tecnologias
Linguagens: Go, Python
Frameworks: gRPC, Gin
Cloud: AWS (EKS, Lambda, SQS)
Mensageria: Kafka, RabbitMQ

Pontos fortes
- Longa experiencia com Go (8 anos)
- Atuacao em fintech de grande porte com sistemas criticos
- Experiencia com arquitetura distribuida e alta disponibilidade

Pontos de atencao
- Salary pode estar acima da faixa para seniority
- Disponibilidade para modelo hibrido/presencial precisa ser validada

Recomendacao
[OK] Recomendo avancar para entrevista tecnica, para validar:
- Detalhes de arquitetura dos sistemas de pagamentos
- Experiencia com escalabilidade e resiliencia

### RUIM
Input: Parecer para Rafael

Output:
Resumo do perfil
Rafael e developer Go.

Problemas: Sem informacoes especificas, avaliacao vaga.
</examples>
</skill>
