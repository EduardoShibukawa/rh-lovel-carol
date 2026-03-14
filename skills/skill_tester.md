<skill id="TESTER">

**Objetivo:**
Executar testes automatizados nos prompts de tests_prompts/ para validar qualidade antes de aplicar ao projeto original.

**Autoridades aplicáveis:**
- Test-Prompt (TDD for LLM instructions): Isolated subagents como clean slate
- Maxim AI: Side-by-side comparison, version tracking, diff between versions
- Evaligo: Build a Test Dataset, Define Success Criteria, Evaluate Systematically

---

<fluxo>
  1. CARREGAR prompts de tests_prompts/ (não os originais)
  2. IDENTIFICAR qual skill/module está sendo testado (POST/OUTREACH/HUNTING)
  3. SELECIONAR fixture de teste apropriado em tests/fixtures/
  4. EXECUTAR o prompt com a fixture (via subagent em contexto limpo)
  5. COMPARAR output com resultado esperado em tests/results/
  6. GERAR relatório de diff: melhorou / piorou / inalterado
  7. SE aprovado, COPIAR para prompts/ (só após validação)
</fluxo>

<test_runner>
  Ao executar o teste, você DEVE:
  - Usar subagent para executar em contexto limpo (sem viés de conversa anterior)
  - Usar as fixtures existentes: tests/fixtures/*.md
  - Comparar com os resultados esperados: tests/results/*.md
  - Reportar métricas: precisão, tom, completude, compliance
</test_runner>

<validacao_criteria>
  Para cada teste, avaliar:
  
  ✓ FORMATO: Estrutura esperada seguida?
  ✓ TOM: Tom humano, sem formalismo?
  ✓ TRANSPARÊNCIA: Salary em faixa explícita?
  ✓ AUTORIDADES: Referências corretas aplicadas?
  ✓ LINK: Invite parameter presente?
  
  Cada critério = 1 ponto. Score mínimo: 4/5 para aprovação.
</validacao_criteria>

<diff_report>
  O relatório DEVE incluir:
  - Fixture usada
  - Resultado anterior vs atual
  - Score (X/5)
  - Status: APROVADO / REPROVADO / APROVADO COM RESSALVAS
  - Se reprovado: lista de problemas específicos
  - Recomendação: aplicar ao projeto ou revisar
</diff_report>

<exemplo_test>
  TESTE: skill_post.md com fixture exemplo_1_vagas_tech
  
  Executando em contexto limpo...
  
  📊 RESULTADO:
  - Formato: ✓ Segue estrutura
  - Tom: ✓ Humano, direto
  - Transparência: ✓ Faixa salarial explícita
  - Autoridades: ✓ Lou Adler hook aplicado
  - Link: ✓ Com invite parameter
  
  Score: 5/5 - APROVADO
  
  💡 Recomendação: Pode aplicar ao projeto original.
</exemplo_test>

<confidence>
  Score: 9/10
  Reasoning: Segue metodologia Test-Prompt (isolated subagents), usa fixtures existentes, compara com results esperados, gera diff report. Baseado em Maxim AI e Evaligo best practices.
  References: Test-Prompt (MCP Market), Maxim AI, Evaligo
</confidence>

</skill>