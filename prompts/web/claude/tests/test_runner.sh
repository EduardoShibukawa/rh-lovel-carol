#!/bin/bash
# Test Runner para Claude Skills
# Usage: ./test_runner.sh [skill] [fixture]

echo "========================================"
echo "🧪 TEST RUNNER - CLAUDE SKILLS"
echo "========================================"

SKILL=$1
FIXTURE=$2

if [ -z "$SKILL" ] || [ -z "$FIXTURE" ]; then
    echo "Usage: ./test_runner.sh [hunting|outreach|post] [fixture_name]"
    echo ""
    echo "Available skills:"
    echo "  - hunting"
    echo "  - outreach"
    echo "  - post"
    echo ""
    echo "Available fixtures:"
    ls -1 tests/fixtures/
    exit 1
fi

echo "Skill: $SKILL"
echo "Fixture: $FIXTURE"
echo "========================================"

# Verificar se arquivos existem
if [ ! -f "$SKILL/SKILL.md" ]; then
    echo "❌ Skill não encontrada: $SKILL/SKILL.md"
    exit 1
fi

if [ ! -f "tests/fixtures/$FIXTURE.md" ]; then
    echo "❌ Fixture não encontrada: tests/fixtures/$FIXTURE.md"
    exit 1
fi

echo "✅ Arquivos encontrados"
echo ""

# Mostrar conteúdo da fixture
echo "📥 FIXTURE:"
echo "---"
cat "tests/fixtures/$FIXTURE.md"
echo "---"
echo ""

# Mostrar critérios de validação
echo "📋 CRITÉRIOS DE VALIDAÇÃO:"
echo "---"

case $SKILL in
    hunting)
        echo "1. Boolean com 5+ sinônimos por termo"
        echo "2. X-Ray search (site:linkedin.com/in)"
        echo "3. Exclusões (NOT júnior/estágio)"
        echo "4. Localização específica (cidade + estado + região)"
        ;;
    outreach)
        echo "1. M1 máximo 200 caracteres"
        echo "2. M2 com salary faixa explícita"
        echo "3. Follow-up Day 4 / Day 7"
        echo "4. Invite parameter presente"
        ;;
    post)
        echo "1. Hook com impacto 90 dias (não cargo)"
        echo "2. Salary faixa explícita"
        echo "3. Máximo 4 vagas por post"
        echo "4. Sem separadores/travessões"
        ;;
esac

echo "---"
echo ""
echo "✅ Test runner configurado"
echo "📝 Para executar: usar Claude com a skill e fixture acima"
