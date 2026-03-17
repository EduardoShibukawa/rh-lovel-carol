---
name: lovel-skill
description: "Melhorar, testar e validar skills existentes. Use para: (1) Executar evals em skills,
(2) Melhorar skills existentes com base em feedback, (3) Comparar versões (A/B), 
(4) Otimizar description para triggering, (5) Benchmark de performance.
Não use para: criar novas skills do zero."
---

# LOVEL SKILL - Gerenciamento de Skills

Skill baseada na skill-creator da Anthropic. Faz tudo que a skill-creator faz, EXETO criar skills do zero.

## Overview

Metodologia completa para:
1. **Avaliar** - Executar evals e medir performance
2. **Melhorar** - Iterar sobre skills com base em feedback
3. **Comparar** - A/B testing entre versões
4. **Otimizar** - Description para triggering

---

## Fluxo Principal

### 1. DETECTAR O QUE FAZER
Perguntar ao usuário:
- "Quer melhorar uma skill existente ou executar evals?"
- "Tem uma versão anterior para comparar?"

### 2. CARREGAR SKILL
Identificar qual skill trabalhar:
- `lovel-hunting` → hunting/SKILL.md
- `lovel-outreach` → outreach/SKILL.md
- `lovel-post` → post/SKILL.md
- `lovel-parecer` → parecer/SKILL.md

### 3. EXECUTAR EVALS
Para cada eval em `evals/evals.json`:
1. Ler prompt
2. Executar skill
3. Comparar com expected_output
4. Registrar resultado

### 4. AVALIAR RESULTADOS
- Mostrar outputs ao usuário
- Coletar feedback qualitativo
- Identificar problemas

### 5. MELHORAR (se necessário)
Com base no feedback:
- Revisar instruções
- Adicionar/remover exemplos
- Ajustar workflow
- Rerun evals

---

## Estrutura de Evals

Cada skill tem `evals/evals.json`:

```json
{
  "skill_name": "lovel-hunting",
  "evals": [
    {
      "id": 1,
      "prompt": "Go/Golang Senior...",
      "expected_output": "Boolean com 5+ sinônimos..."
    }
  ]
}
```

### Executar Eval

1. Ler `skill/evals/evals.json`
2. Para cada eval:
   - Executar skill com o prompt
   - Comparar output com expected
   - Marcar PASSOU / FALHOU

### Gerar Relatório

```
📊 EVAL - [SKILL]

Eval: [ID] - [nome]
Prompt: [prompt]
Expected: [critério]
Result: ✅ PASSOU / ❌ FALHOU

[Se falhou]: Problema: [o que faltou]
```

---

## Comparação A/B (Blind)

Para comparar duas versões:

1. **Versão A**: Skill atual
2. **Versão B**: Versão anterior ou alternativa

Executar ambas com mesmo prompt e pedir para usuário escolher melhor.

### Estrutura:

```
📊 COMPARAÇÃO A/B

Prompt: [mesmo para ambos]

--- VERSÃO A ---
[output]

--- VERSÃO B ---
[output]

Escolha: [A / B / Empate]
Por quê: [razão]
```

---

## Melhoria de Skills

### Passo 1: Coletar Feedback
O que o usuário quer mudar?
- Estrutura?
- Exemplos?
- Workflow?
- Limitations?

### Passo 2: Aplicar Melhorias
Editar skill com base no feedback

### Passo 3: Rerun Evals
Executar evals novamente para verificar se melhorou

### Passo 4: Validar
- Score melhorou?
- Problemas resolvidos?
- Nenhum problema novo criado?

---

## Otimização de Description

Para melhorar triggering:

### Passo 1: Gerar Queries de Teste
Criar 10-20 exemplos:
- Should trigger (8-10)
- Should NOT trigger (8-10)

### Passo 2: Testar
Verificar se skill dispara quando deveria

### Passo 3: Ajustar
Melhorar description com base nos resultados

---

## Evals por Skill

### lovel-hunting
| ID | Prompt |
|----|--------|
| 1 | Go/Golang Senior |
| 2 | SDR/BDR Curitiba |
| 3 | QA Engineer Playwright |

### lovel-outreach
| ID | Prompt |
|----|--------|
| 1 | M1 SDR |
| 2 | M1 Developer |
| 3 | Follow-up Day 4 |

### lovel-post
| ID | Prompt |
|----|--------|
| 1 | Vaga Go Senior |
| 2 | 3 vagas |
| 3 | Salary único |

### lovel-parecer
| ID | Prompt |
|----|--------|
| 1 | Levi Alves QA |
| 2 | Jason Pires Tech Lead |

---

## Limitations

- **NÃO criar** skills do zero (use skill-creator para isso)
- **SEMPRE** executar evals antes de declarar "pronto"
- **NUNCA** ignorar feedback do usuário
- **DOCUMENTAR** mudanças no changelog

## Validation

- [ ] Evals executados?
- [ ] Feedback coletado?
- [ ] Melhorias aplicadas?
- [ ] Rerun realizado?
- [ ] Score melhorou?
