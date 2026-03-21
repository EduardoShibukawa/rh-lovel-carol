<skill>
<name>skill_outreach</name>
<description>DMs personalizadas, follow-up e cadência de outreach. Use para: (1) Escrever mensagem inicial (M1), (2) Criar detalhamento (M2), (3) Definir follow-up (Day 4, Day 7), (4) Personalizar para candidato específico. Não use para: criar boolean queries, escrever posts, analisar CVs.</description>

<instructions>
REGRAS OBRIGATORIAS:
1. M1 maximo 200 caracteres
2. M2 com salary faixa (R$ Xk – R$ Yk) E invite=caroline.lima798
3. Follow-up deve conter "Day 4" ou "Day 7" explicitamente
4. Tom humano, direto, sem formalismo
5. Maximo 1 emoji por mensagem

OUTPUT para M1:
M1: Oi [Nome]! Sou Carol da Lovel. Vi seu perfil e acredito que possa interessar: [Vaga]. Top?

OUTPUT para M2:
M2: Perfeito! Mais detalhes:

Empresa: [Nome]
Cargo: [Titulo]
Stack: [Tecnologias]
Modelo: [Presencial/Hibrido/Remoto] | [Cidade]
Salary: R$ Xk – R$ Yk | [CLT/PJ]

Faz sentido? [link com invite=caroline.lima798]

OUTPUT para Follow-up:
Follow-up Day 4: Oi [Nome]! Passando pra ver se viu
Follow-up Day 7: Oi [Nome]! Entendo se nao for o momento. Boa sorte!
</instructions>

<examples>
### BOM - M1
Input: M1 para Rafael - Dev Go Sr - R$18k-25k

Output:
M1: Oi Rafael! Sou Carol da Lovel. Vi seu perfil e acredito que possa interessar: Dev Go Sr R$18k-25k. Top?

### BOM - M2
Input: M2 para Rafael - DevGo Sr - Nubank - R$18k-25k - CLT

Output:
M2: Perfeito! Mais detalhes:

Empresa: Nubank
Cargo: DevGo Sr
Stack: Go, gRPC, Kafka
Modelo: Hibrido | Sao Paulo
Salary: R$ 18k – R$ 25k | CLT

Faz sentido? app.lovel.dev/vaga?invite=caroline.lima798

### BOM - Follow-up Day 4
Input: Follow-up Day 4 para Rafael (sem resposta)

Output:
Follow-up Day 4: Oi Rafael! Passando pra ver se viu

### BOM - Follow-up Day 7
Input: Follow-up Day 7 para Ana (sem resposta final)

Output:
Follow-up Day 7: Oi Ana! Entendo se nao for o momento. Boa sorte!

### RUIM
Input: M1 para Rafael

Output:
Prezado Rafael,
Gostaria de apresentar uma oportunidade incrível em uma empresa líder de mercado...

Problemas: Formal demais, muitos caracteres, tom corporate.
</examples>

<proibido>
- Mais de 200 caracteres na M1
- Mais de 1 emoji por mensagem
- Formalismo ("Prezado", "Caro")
- Salary "a combinar"
</proibido>
</skill>
