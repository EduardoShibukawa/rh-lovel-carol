# Grader Agent

Como avaliar outputs:

1. Leia eval_metadata.json
2. Leia output gerado
3. Para cada assertion:
   - Verifique se atende critério
   - Marque passed: true/false
   - Adicione evidence

Output em grading.json:
```json
{
  "eval_id": 0,
  "expectations": [{"text": "...", "passed": true, "evidence": "..."}]
}
```
