# Esquemas JSON

## evals.json
```json
{
  "skill_name": "example",
  "evals": [{"id": 1, "prompt": "...", "expected_output": "..."}]
}
```

## grading.json
```json
{
  "eval_id": 0,
  "expectations": [{"text": "...", "passed": true, "evidence": "..."}]
}
```

## benchmark.json
```json
{
  "skill_name": "...",
  "timestamp": "...",
  "iterations": [...]
}
```
