---
name: lovel-outreach
description: "DMs personalizadas, follow-up e cadência de outreach. 
Use para: (1) Escrever mensagem inicial (M1), (2) Criar detalhamento (M2), 
(3) Definir follow-up (Day 4, Day 7), (4) Personalizar para candidato específico.
Não use para: criar boolean queries, escrever posts, analisar CVs."
---

# OUTREACH

## INPUT

Extraia do prompt:
- `name`: nome do candidato (se desconhecido, usar "oi")
- `title`: titulo da vaga (ex: Java Backend Sr)
- `salary`: faixa salarial (ex: R$ 10k-13k)
- `stack`: tecnologias principais
- `model`: remoto/híbrido/presencial
- `city`: cidade se aplicavel

**Regras para campos ausentes:**
- Se `name` ausente: usar "oi" (não "Prezado")
- Se `salary` ausente: omitir de M1, incluir range estimado em M2
- `model` default: remoto
- `contract` default: CLT (usar PJ apenas se explicitamente solicitado)

## Regras

1. M1 maximo 200 caracteres
2. M2 com salary faixa + invite=no_link
3. Maximo 1 emoji por mensagem
4. Tom humano, direto, sem formalismo
5. Follow-up contem "Day 4" ou "Day 7"

## MENSAGENS

### M1 (ate 200 caracteres)
```
Oi [Nome]! Sou Carol da Lovel. Vi seu perfil e acredito que possa interessar: [Titulo] [Salary]. Top?
```

### M1 Personalizado (ate 200 caracteres)
```
Oi [Nome]! Vi seu background em [tecnologia especifica] e acredito que possa interessar: [Titulo]. Top?
```

### M2
```
Perfeito! Mais detalhes:

Empresa: [Nome da Empresa]
Cargo: [Titulo]
Stack: [Tecnologias]
Modelo: [Remoto/híbrido/presencial] | [Cidade]
Salary: R$ Xk – R$ Yk | [CLT/PJ]

Faz sentido? app.lovel.dev/vaga?invite=caroline.lima798
```

### Follow-up
```
Follow-up Day 4: Oi [Nome]! Passando pra ver se viu 😊
Follow-up Day 7: Oi [Nome]! Entendo se não for o momento. Boa sorte!
```

## EXEMPLOS

### Exemplo 1: M1 Padrao
**Input:** "M1 para Carlos - Java Backend Sr - R$10k-13k"

```
M1: Oi Carlos! Sou Carol da Lovel. Vi seu perfil e acredito que possa interessar: Java Backend Sr R$10k-13k. Top?
```

### Exemplo 2: M1 Personalizado
**Input:** "M1 para Rafael - Tech Lead Python - vi que trabalhou na Nubank"

```
M1: Oi Rafael! Vi que atuava na Nubank e acredito que possa interessar: Tech Lead Python. Top?
```

### Exemplo 3: M2 Completo
**Input:** "M2 para Carlos - Nubank - Java Sr - R$10k-13k - híbrido SP"

```
M2: Perfeito! Mais detalhes:

Empresa: Nubank
Cargo: Backend Engineer Sr
Stack: Java, Spring Boot, AWS
Modelo: Hibrido | São Paulo
Salary: R$ 10k – R$ 13k | CLT

Faz sentido? app.lovel.dev/vaga?invite=caroline.lima798
```

### Exemplo 4: M1 Sem Nome
**Input:** "M1 para candidato invisível - Go Senior - R$15k-20k"

```
M1: Oi! Vi seu perfil e acredito que possa interessar: Go Senior R$15k-20k. Top?
```

### Exemplo 5: Follow-up
**Input:** "Follow-up Day 4 para Rafael"

```
Follow-up Day 4: Oi Rafael! Passando pra ver se viu 😊
```

## O que não fazer

- M1 com mais de 200 caracteres
- Mais de 1 emoji por mensagem
- Formalismo ("Prezado", "Caro", "Atenciosamente")
- Salary "a combinar"
- Emojis em M2 (apenas em M1 e Follow-up)
