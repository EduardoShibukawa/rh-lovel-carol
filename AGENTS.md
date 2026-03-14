# 🧠 AGENTS.md — Ecossistema de Hunting Lovel (Carol Lima)

Este documento descreve a arquitetura, as autoridades e os princípios fundamentais do sistema de prompts projetado para escalar a operação de Tech Recruiting da Carol Lima na Lovel.

---

## 🚀 Objetivo do Projeto
Transformar a atividade de hunting (busca, atração e abordagem) em um processo de alta performance, unindo o **DNA da Lovel** (Transparência/DX), a **Essência da Carol** (Humanidade/Diretividade) e a ciência das **Autoridades Mundiais** de recrutamento.

---

## 📁 Estrutura de Arquivos

```
rh-carol/
├── Makefile                     # Automação de testes e sincronização
├── AGENTS.md                    # Este arquivo
├── prompts/                     # Prompts ORIGINAIS (PRODUÇÃO)
│   ├── authorities.md           # 6 autoridades de recrutamento validadas
│   ├── system_prompt.md         # Identidade + Roteador + DNA Lovel
│   └── skills/
│       ├── skill_post.md        # Lou Adler + Lovel
│       ├── skill_outreach.md    # Stacy Zapar + Lovel
│       └── skill_hunting.md     # Glen Cathey + Aaron Ross + Gergely Orosz + Lovel
├── tests_prompts/               # Cópia para teste (DESENVOLVIMENTO)
│   ├── authorities.md
│   ├── system_prompt.md
│   └── skills/
├── tests/
│   ├── fixtures/                # Entradas de exemplo para validação
│   └── results/                 # Resultados esperados (Golden Sets)
└── skills/
    └── skill_tester.md          # Skill de testes automatizados
```

---

## 📊 Arquitetura Visual (Fluxo de Decisão)

```mermaid
graph TD
    A[Carol cola Vaga/Briefing] --> B[system_prompt.md]
    
    subgraph "Detector & Router"
    B -->|Detecta Formato| C[Multi-vaga Lovel]
    B -->|Detecta Formato| D[Briefing Individual]
    B -->|Detecta Formato| E[Entrada Ambígua]
    end

    C & D --> F[Pergunta de Confirmação]
    E --> G[Pede mais detalhes]
    
    F -->|Comando: Hunting| H[skill_hunting.md]
    F -->|Comando: Post| I[skill_post.md]
    F -->|Comando: Outreach| J[skill_outreach.md]
    
    subgraph "Módulos de Inteligência"
    H --> H1[Queries Booleanas validadas]
    I --> I1[LinkedIn Post - Impacto 90 dias]
    J --> J1[DM Personalizada 3x3]
    end
    
    H1 & I1 & J1 --> K[authorities.md - Validação]
    K --> L[PROTOCOLO MENTOR]
    
    L --> M[Pergunta Estratégica]
    L --> N[Próximo Passo / Nudge]
    L --> O[Por quê? - Autoridades]
    
    M & N & P --> Q[Execução de Alta Performance]
```

---

## 🛠️ Fluxo de Trabalho e Sourcing (OODA Loop)

### Sincronização e Testes (TDD para Prompts)
O projeto utiliza um fluxo de **Test-Driven Development** para garantir que alterações nos prompts não quebrem as "Regras de Ouro".

1. **Desenvolvimento**: Altere os prompts apenas em `tests_prompts/`.
2. **Validação**: Use o `Makefile` para verificar conformidade (ex: ausência de travessões).
3. **Promoção**: Após validado, use `make sync` para mover para `prompts/`.

```bash
make lint    # Verifica erros de estilo (ex: travessões proibidos)
make sync    # Promove prompts de tests_prompts/ para prompts/
make test    # (Em breve) Executa validações contra fixtures
```

---

## 💎 Princípios Inegociáveis (DNA Lovel)

*   **Transparência Radical:** Salário sempre exposto em faixa normalizada (ex: R$ 10k – R$ 14k).
*   **Atribuição de Invite:** Preservação obrigatória do parâmetro `invite=caroline.lima798`.
*   **Voz Humana:** **PROIBIDO** o uso de travessões (`—`), jargões corporativos ("dinâmico", "oportunidade incrível") e formalismo excessivo.
*   **Detector de Input:** O sistema sempre confirma a intenção da Carol antes de executar.

---

## 📚 Autoridades de Referência

| Autoridade | Princípio | Aplicação |
|------------|-----------|-----------|
| **Lou Adler** | Performance-based Hiring | Títulos baseados em impacto de 90 dias |
| **Stacy Zapar** | 3x3 Rule | Outreach personalizado e cadência |
| **Glen Cathey** | Boolean Black Belt | Queries de sourcing avançadas |
| **Aaron Ross** | Predictable Revenue | ICP e prospecção outbound |
| **Gergely Orosz** | Pragmatic Engineer | Mindset e linguagem para talentos tech |
| **Lovel** | DNA & Speed | SLA 10 dias, Transparência, IA Copilot |

---

## 📊 Score de Qualidade do Projeto
**Score Atual:** 9.5/10
**Confidence Score:** 9.2/10
**Tipo de projeto:** Repositório de Engenharia de Prompts (Prompts-as-Code)

---
**Última atualização:** 2026-03-14
