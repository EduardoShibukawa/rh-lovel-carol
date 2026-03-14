<skill id="TESTER">

**Objetivo:**
Executar testes automatizados nos prompts de tests_prompts/ para validar qualidade antes de aplicar ao projeto original.

**Autoridades aplicáveis:**
- Test-Prompt (TDD for LLM instructions): Isolated subagents como clean slate
- Maxim AI: Side-by-side comparison, version tracking, diff between versions
- Evaligo: Build a Test Dataset, Define Success Criteria, Evaluate Systematically

---

<fluxo>
  1. DETECTAR mudanças: Usar git diff para identificar quais arquivos foram alterados em tests_prompts/
  2. IDENTIFICAR qual skill foi modificado (POST/OUTREACH/HUNTING/system_prompt)
  3. SELECIONAR fixture de teste apropriado em tests/fixtures/
  4. EXECUTAR o prompt com a fixture (via subagent em contexto limpo)
  5. VALIDAR AUTOMATICAMENTE os critérios abaixo
  6. GERAR relatório com links de teste
  7. SE aprovado, COPIAR para prompts/ (só após validação)
</fluxo>

<detectar_mudancas>
  Antes de testar, execute:
  git diff --name-only tests_prompts/
  
  Mapeamento automático:
  - skill_post.md → testar com fixture_1_vagas_tech
  - skill_outreach.md → testar com fixture_2_vaga_bdr
  - skill_hunting.md → testar com fixture_2_vaga_bdr
  - system_prompt.md → testar todos os skills
  - authorities.md → validar referências nos skills
  
  Se nenhuma mudança detectada: "Nenhuma mudança para testar"
</detectar_mudancas>

<test_runner>
  Ao executar o teste, você DEVE:
  - Usar subagent para executar em contexto limpo (sem viés de conversa anterior)
  - Usar as fixtures existentes: tests/fixtures/*.md
  - Executar o prompt completo e capturar o output
  - VALIDAR TODOS OS CRITÉRIOS automaticamente (veja abaixo)
  - Reportar métricas: precisão, tom, completude, compliance
  - GERAR LINKS DE TESTE para X-Ray queries
</test_runner>

<validacao_automatica>
  **Para TODOS os skills:**
  ✓ FORMATO: Estrutura esperada seguida?
  ✓ TOM: Tom humano, sem formalismo?
  ✓ TRANSPARÊNCIA: Salary em faixa explícita?
  ✓ AUTORIDADES: Referências corretas aplicadas?
  ✓ LINK: Invite parameter presente?
  ✓ PROIBIDO: Travessões (—), separadores (---, ===)

  **Para HUNTING (validação implícita):**
  ✓ SINÔNIMOS: Tem pelo menos 3 sinônimos do cargo?
  ✓ LOCALIZAÇÃO: Tem expansão (cidade + estado + região)?
  ✓ EXCLUSÕES: Tem NOT para excluir júnior/estagiário?
  ✓ X-RAY: Tem query site:linkedin.com?
  ✓ ESTRUTURA: Tem 3-4 variações (Volume, Método, Alternative)?
  → Se X-RAY encontrada: GERAR LINK GOOGLE automaticamente

  **Para POST (validação implícita):**
  ✓ HOOK: Foco em impacto de 90 dias (Lou Adler)?
  ✓ CONTEXTO: Setor ou contexto incluso?
  ✓ EMOJI: Máximo 1 por linha?
  ✓ LIMITE: Máximo 4 vagas por post?

  **Para OUTREACH (validação implícita):**
  ✓ M1: Entre 250-300 caracteres?
  ✓ PERSONALIZAÇÃO: Tem placeholder ou detalhe real?
  ✓ FOLLOWUP: Tem M2 estruturada?
</validacao_automatica>

<diff_report>
  O relatório DEVE incluir:
  - Fixture usada
  - Skill testado
  - Score (X/Y critérios)
  - Status: APROVADO / REPROVADO / APROVADO COM RESSALVAS
  - Problemas específicos (se houver)
  - Links de teste (se aplicável)
  - Recomendação: aplicar ao projeto ou revisar

  **Formato do relatório:**
  ```
  📊 TESTE AUTOMÁTICO - [SKILL]
  Fixture: [nome]
  Score: [X/Y]
  Status: [APROVADO/REPROVADO]
  
  🔗 Links para testar:
  • [link Google]
  
  💡 Recomendação: [sim/não]
  ```
</diff_report>

<confidence>
  Score: 9/10
  Reasoning: Validação implícita para todos os skills (HUNTING, POST, OUTREACH). Gera links de teste automaticamente. Segue metodologia Test-Prompt com subagents.
  References: Test-Prompt (MCP Market), Maxim AI, Evaligo
</confidence>

</skill>