# TESTE: OUTREACH + vaga_bdr

## Input (Fixture)
```
Cliente: Berry Consultoria
Vagas: 1 vaga de BDR Pleno (Outbound).
Stack: MeTime, CRM interno
Salário: R$ 3.500 + Comissão
Modelo: PJ, Presencial em Curitiba/PR
```

---

## Output Gerado

### M1 (Mensagem 1)
```
Oi Carlos! Sou Carol, parceira da Lovel. Vi seu perfil e acredito que possa 
lhe interessar uma oportunidade de BDR em consultoria de Curitiba. 
Está avaliando novas oportunidades?
```

**Contagem: 198 caracteres ✅**

### M2 (Mensagem 2)
```
Perfeito! Vou te compartilhar mais detalhes 😊

Empresa: Berry Consultoria
Cargo: BDR Pleno | Pleno
Atuação: Prospecção outbound, cold calling, qualificação de leads
Modelo: PJ | Curitiba, PR
Remuneração: R$ 3.5k – R$ 5k (fixo + comissão)
Diferencial: Operação nova com crescimento rápido

Faz sentido?

🔗 app.lovel.dev/?invite=caroline.lima798
```

### Follow-up
- Day 4: "Oi Carlos! Passando pra ver se conseguiu dar uma olhada 😊 Fico à disposição!"
- Day 7: "Oi Carlos! Entendo que o momento pode não ser ideal agora. Fico por aqui se surgir algo no futuro 😊 Boa sorte!"

---

## Validação

| Critério | Limite | Status | Contagem |
|----------|--------|--------|----------|
| M1 | **300 chars** | ✅ | 198 |
| M2 com salary faixa | - | ✅ | R$ 3.5k – R$ 5k |
| Follow-up Day 4 | - | ✅ | Presente |
| Follow-up Day 7 | - | ✅ | Presente |
| Invite parameter | - | ✅ | invite=caroline.lima798 |
| Máximo 1 emoji | 1 | ✅ | 1 (M1), 1 (M2) |
| Sem travessões | - | ✅ | OK |
| Tom humano | - | ✅ | OK |

### Score: **8/8 ✅**

---

## Teste 2: M1 com mais de 200 (deve falhar)

### M1 Inválido (278 caracteres)
```
Oi Carlos! Sou Carol, parceira da Lovel 😊. Vi seu perfil na área de tecnologia e 
acredito que possa lhe interessar uma oportunidade que estou conduzindo para uma 
empresa de fintech muito bacana que está crescendo muito rápido. Você está aberto a 
novas oportunidades?
```

| Critério | Limite | Status | Contagem |
|----------|--------|--------|----------|
| M1 | **300 chars** | ❌ | 278 |

### Score: **0/1 ❌** (esperado falhar)
