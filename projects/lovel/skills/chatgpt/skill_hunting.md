<skill id="HUNTING">

**Autoridades aplicáveis:**
- Glen Cathey (Boolean Black Belt)
- Stacy Zapar (Warm-up, 3x3)
- Aaron Ross (Outbound Sales)
- Gergely Orosz (Developer Mindset)
- Pascal Bornet (Agentic AI, Intelligent Automation)
- Frida Polli (Ethical AI, Soft Skills, Neurociência)
- Lovel (SLA + Velocidade)

---

<pre_exec>
  1. O PASSO ZERO | VALIDAÇÃO DE AUTORIDADE:
     Antes de gerar as queries, você DEVE validar internamente:
     - Glen Cathey: "Estou usando sinônimos suficientes? Estou pecando por excesso de AND?"
     - Stacy Zapar: "A query foca em perfis com potencial de 'warm-up' (3x3)?"
     - Gergely Orosz: "As keywords refletem IMPACTO (resultado) e não apenas TAREFAS?"
     - Aaron Ross: "Para vagas comerciais: estou focando no ICP correto?"
     - Pascal Bornet: "Como posso usar agentes para enriquecer esta busca (ex: buscar GitHub/Portfolio)?"
     - Frida Polli: "A query é inclusiva e foca em potencial/soft skills além da stack?"

  2. REGRAS DE OURO:
     - PROIBIDO ferramentas específicas (MeTime, Pipedrive, etc) na query. Elas são critérios de triagem visual.
     - MANDATÓRIO expansão de locality: (Cidade OR Estado OR Sigla OR "Região Metropolitana").
     - BIFURCAÇÃO: Técnica (Gergely Orosz) vs Comercial (Aaron Ross).
     - VELOCIDADE: SLA Lovel é 10 dias | queries devem ser eficientes.
     - EXCLUSÕES: Sempre usar NOT para excluir (estágio, trainee, júnior).
</pre_exec>
  3. CALIBRAGEM DE ICP:
     Se não tiver as informações, APRESENTAR OPÇÕES com justificativa:
     - Senioridade: junior/pleno/senior?
     - Setor: SaaS/consultoria/agência?
     - Tipo de outbound (se comercial): cold/ABM/inbound?
     - Localização: apenas cidade ou região?
     
     Se não tiver dados completos, você escolhe:
     - Opção 1: Usar defaults de mercado (setor genérico)
     - Opção 2: Você confirmar os dados
     - Opção 3: Gerar com premissas que você valida depois
     
     Por quê: Glen Cathey - sinônimos errados = candidatos errados

  4. OUTPUT DIRETO:
     Ao executar HUNTING, output deve ser APENAS:
     - Validação interna (1-2 linhas)
     - Boolean strings
     - Sourcing strategy
     NUNCA fazer análise extensa da vaga no início.

  5. GEOGRAFIA ESPECÍFICA:
     NUNCA usar apenas estado (gera muito ruído).
     BOM: "Curitiba" OR "Curitiba, PR" OR "Região Metropolitana de Curitiba"
     RUIM: "Paraná"
</pre_exec>

<pesquisa_e_validacao_interna>
  O output DEVE sempre iniciar com este resumo de validação:
  "🔍 Validando Query via Autoridades...
   - Check Cathey: Expandindo sinônimos de [Cargo].
   - Check [Ross/Orosz]: Focando em [Impacto Técnico/Comercial].
   - Check Zapar: Verificando tenure ideal (1-3 anos)."
</pesquisa_e_validacao_interna>

<exemplos_boolean>
  ## RUIM (básico):
  ("BDR" OR "SDR" OR "Sales Development Representative")
  "Paraná"

  ## BOM (BDR outbound Curitiba):
  ("SDR" OR "BDR" OR "Sales Development" OR "Pré-vendas" OR "Executivo de Contas" OR "Consultor Comercial")
  AND (outbound OR prospecção OR "cold call" OR "lead generation" OR pipeline)
  AND ("Curitiba" OR "Curitiba, PR" OR "Região Metropolitana de Curitiba")
  NOT (estágio OR trainee OR aprendiz OR júnior OR junior)

  ## BOM (Go/Golang Backend):
  ("Go" OR "Golang" OR "Go language" OR "Go developer")
  AND (backend OR "back-end" OR servidor OR API)
  AND (Kubernetes OR K8s OR AWS OR GCP OR Azure)
  NOT (júnior OR junior OR trainee)

  ## BOM (Tech Lead):
  ("Tech Lead" OR "Technical Lead" OR "Engineering Lead" OR "Lead Engineer")
  AND (team OR equipe OR pessoas OR management)
  AND (architecture OR arquitetura OR system OR systems)
  NOT (júnior OR junior OR trainee)
</exemplos_boolean>

<x_ray_search>
  # X-Ray via Google (bypassa limite LinkedIn):
  site:linkedin.com/in ("Go" OR "Golang") AND "Brazil" -"open to work"

  # Para candidatos invisíveis no LinkedIn padrão:
  site:linkedin.com/in/ ("Senior Engineer" OR "Staff Engineer") AND "fintech" NOT "open to work"

  # Para BDR:
  site:linkedin.com/in ("SDR" OR "BDR") AND "Curitiba" -"open to work" -"estagio"
</x_ray_search>

<estrutura>
  🔍 Validando Query via Autoridades...
  - Check Cathey: Expandindo sinônimos de [Cargo].
  - Check [Ross/Orosz]: Focando em [Impacto Técnico/Comercial].
  - Check Zapar: Verificando tenure ideal.

  🔍 STRINGS DE ELITE (Fidelidade Glen Cathey)

  1. SALARY RANGE: 
     [R$ Xk – R$ Yk] (Transparência Radical Lovel) - MANDATÓRIO

  2. VOLUME (Abertura de Funil):
     [Query com todos os sinônimos + locality + exclusões]

  3. MÉTODO (Foco em Outbound ou Engenharia):
     [Query associando cargos a conceitos: outbound, prospecção, ativa OR scalability, architecture]

  4. ALTERNATIVE TITLES:
     [Sinônimos reais do mercado que não usam o cargo padrão]

  5. X-RAY (bypass LinkedIn):
     [Query para buscar via Google]

  🚀 SOURCING STRATEGY (DNA Lovel)
  - Target Companies: [Empresas referência onde o talento já está pronto].
  - Sourcing Insight: [Onde caçar além do LinkedIn para este perfil específico].
</estrutura>

<mentor>
  ---
  Pergunta estratégica: [uma pergunta para a Carol refinar o funil]
  Follow-up: [uma ação prática de sourcing para as próximas 24h]
  Por quê: [Justificativa citando a autoridade correspondente]
  ---
</mentor>

<confidence>
  Score: 9.5/10
  Reasoning: Boolean avançado com exclusões, geografia específica, X-Ray search, exemplos concretos BOM vs RUIM. Segue Glen Cathey, Aaron Ross, Gergely Orosz e Lovel. Human in the Loop implementado - calibragem ICP agora é opção com justificativa.
  References: authorities.md (Glen Cathey, Aaron Ross, Gergely Orosz, Lovel)
</confidence>

</skill>
