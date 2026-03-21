---
name: lovel-outreach
description: "DMs personalizadas, follow-up e cadência de outreach. 
Use para: (1) Escrever mensagem inicial (M1), (2) Criar detalhamento (M2), 
(3) Definir follow-up (Day 4, Day 7), (4) Personalizar para candidato específico.
Não use para: criar boolean queries, escrever posts, analisar CVs."
---

# OUTREACH

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

EXEMPLO M1 (ate 200 caracteres):
M1: Oi Carlos! Sou Carol da Lovel. Vi seu perfil e acredito que possa interessar: Java Backend Sr R$10k-13k. Top?

EXEMPLO M2:
M2: Perfeito! Mais detalhes:

Empresa: Nubank
Cargo: Backend Engineer Sr
Stack: Java, Spring Boot, AWS
Modelo: Hibrido | Sao Paulo
Salary: R$ 10k – R$ 13k | CLT

Faz sentido? app.lovel.dev/vaga?invite=caroline.lima798

EXEMPLO FOLLOW-UP:
Follow-up Day 4: Oi Rafael! Passando pra ver se viu
Follow-up Day 7: Oi Rafael! Entendo se nao for o momento. Boa sorte!

PROIBIDO:
- Mais de 200 caracteres na M1
- Mais de 1 emoji por mensagem
- Formalismo ("Prezado", "Caro")
- Salary "a combinar"
