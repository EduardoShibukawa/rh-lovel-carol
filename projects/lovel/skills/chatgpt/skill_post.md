<skill>
<name>skill_post</name>
<description>LinkedIn Posts com impacto de 90 dias, transparência salarial e DNA Lovel. Use para: (1) Criar posts para vagas tech, (2) Escrever hooks baseados em resultados de 90 dias, (3) Estruturar posts com salary explícito, (4) Formatar para LinkedIn. Não use para: escrever outreach, criar boolean queries, analisar CVs.</description>

<instructions>
REGRAS OBRIGATORIAS:
1. HOOK COM "90 DIAS" - O hook DEVE conter "90 dias" ou "em 90 dias"
2. Salary em faixa: R$ Xk – R$ Yk
3. Invite: invite=caroline.lima798
4. ZERO em-dash (—)
5. ZERO separadores (---, ===)

HOOK (OBRIGATORIO):
O hook é a primeira linha e DEVE conter "90 dias" para mostrar impacto.

ESTRUTURA:
[Hook com "90 dias"]

R$ Xk – R$ Yk | CLT/PJ | Senior/Pleno
Modelo | Cidade
Stack principal
app.lovel.dev/vaga?invite=caroline.lima798
</instructions>

<examples>
### BOM
Input: Post para Dev Go Sr - R$18k-25k - CLT - Sao Paulo - Go, AWS, Kubernetes

Output:
Tornar a API 3x mais rápida em 90 dias

R$ 18k – R$ 25k | CLT | Sênior
Híbrido | São Paulo, SP
Go, AWS, Kubernetes
app.lovel.dev/vaga?invite=caroline.lima798

### BOM
Input: Post para DevOps - R$12k-18k - PJ - Remoto - AWS, Terraform, Kubernetes

Output:
Implementar infraestrutura como código em 90 dias

R$ 12k – R$ 18k | PJ | Pleno
Remoto | Brasil
AWS, Terraform, Kubernetes
app.lovel.dev/vaga?invite=caroline.lima798

### BOM
Input: Post para Backend Go - R$15k-22k - CLT - Remoto - Go, Kafka

Output:
Escalar sistemas de pagamentos em 90 dias

R$ 15k – R$ 22k | CLT | Sênior
Remoto | Brasil
Go, Kafka, PostgreSQL
app.lovel.dev/vaga?invite=caroline.lima798

### RUIM
Input: Post para Dev Go Sr

Output:
Senior Backend Engineer

R$ 18k – R$ 25k | CLT
Híbrido | São Paulo
Go, AWS

Problemas: Cargo como hook (deve ter "90 dias").
</examples>

<checklist>
- Hook com "90 dias"
- Salary R$ Xk – R$ Yk
- invite=caroline.lima798
- Zero em-dash (—)
</checklist>
</skill>
