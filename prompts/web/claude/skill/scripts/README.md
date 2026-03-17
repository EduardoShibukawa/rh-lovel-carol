# Scripts - Lovel Skill Management

Scripts Python para gerenciar, testar e validar skills do projeto rh-carol.

Baseados na skill-creator da Anthropic.

## Scripts Disponíveis

### quick_validate.py
Validação rápida de estrutura de skills.
```bash
python scripts/quick_validate.py
```

### run_eval.py
Executa evals para uma skill específica.
```bash
python scripts/run_eval.py ../hunting
```

### aggregate_benchmark.py
Agrega resultados de benchmarks.
```bash
python scripts/aggregate_benchmark.py ../workspace lovel-hunting
```

### improve_description.py
Analisa e sugere melhorias na description.
```bash
python scripts/improve_description.py ../hunting
```

## Uso

### Validar todas as skills
```bash
cd prompts/web/claude/skill/scripts
python quick_validate.py
```

### Executar evals
```bash
python run_eval.py ../hunting
python run_eval.py ../outreach
python run_eval.py ../post
```

## Requisitos

- Python 3.8+
- (Futuro: Claude API para execução automática)
