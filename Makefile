# Makefile para rh-carol (Prompt Engineering)

# Configurações
PROMPTS_DIR = prompts
TEST_PROMPTS_DIR = tests_prompts

.PHONY: help lint sync test init

help:
	@echo "Comandos disponíveis:"
	@echo "  make lint    - Verifica regras de ouro (travessões, invite, etc)"
	@echo "  make sync    - Promove prompts de tests_prompts/ para prompts/"
	@echo "  make init    - Inicializa estrutura de tests_prompts caso não exista"

lint:
	@echo "🔍 Verificando Regras de Ouro..."
	@echo "--- Verificando travessões proibidos (—) ---"
	@! grep -r "—" $(TEST_PROMPTS_DIR) $(PROMPTS_DIR) || (echo "❌ Erro: Travessões (—) encontrados!" && exit 1)
	@echo "✅ Nenhum travessão encontrado."
	@echo "--- Verificando parâmetro de invite Lovel ---"
	@grep -r "invite=caroline.lima798" $(TEST_PROMPTS_DIR) > /dev/null || (echo "❌ Erro: Invite parameter ausente!" && exit 1)
	@echo "✅ Invite parameter encontrado."
	@echo "--- Verificando DNA de Transparência (Salário) ---"
	@grep -r "R\$$" $(TEST_PROMPTS_DIR) > /dev/null || (echo "⚠️ Aviso: Verifique se há faixas salariais nos prompts/fixtures." && exit 0)
	@echo "✅ DNA Lovel presente."
	@echo "--- Verificando Markdown Lint ---"
	@npx markdownlint-cli2 "**/*.md" || echo "⚠️ Markdown style issues found."
	@echo "🚀 Lint completo!"

sync: lint
	@echo "🔄 Sincronizando tests_prompts para prompts (PROMOÇÃO)..."
	cp -rv $(TEST_PROMPTS_DIR)/* $(PROMPTS_DIR)/
	@echo "✅ Sincronização concluída!"

init:
	mkdir -p $(TEST_PROMPTS_DIR)/skills
	cp -rv $(PROMPTS_DIR)/* $(TEST_PROMPTS_DIR)/
	@echo "✅ Estrutura de testes inicializada."

test:
	@echo "🛠️ Executando Test Runner (via skill_tester.md)..."
	@echo "Nota: Este comando requer um LLM para processar os subagents de teste."
	@echo "Consulte tests/fixtures e compare com tests/results."
