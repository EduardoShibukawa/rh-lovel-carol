#!/usr/bin/env python3
"""
Lovel Eval Runner - Deterministic Validation.

Este script executa evals de skills Lovel usando validação determinística
via scripts Python (não usa LLM para grading).

Usage:
    python run_eval.py <skill> [iterations]
    python run_eval.py hunting
    python run_eval.py hunting 3

Args:
    skill: Nome da skill (hunting, outreach, post, parecer)
    iterations: Número de vezes para executar cada eval (default: 1)

Returns:
    Summary com pass rate, avg score, e estatísticas.
"""

import json
import re
import statistics
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

import llm_client

ROOT = Path(__file__).resolve().parent.parent.parent.parent
VALIDATOR_SCRIPT = ROOT / "skills/lovel-tester/scripts/validators/dynamic_validator.py"


def find_evals(target: str) -> Tuple[Optional[Dict], Optional[Path]]:
    """
    Encontra evals baseado no target.
    
    Args:
        target: Nome da skill, platform, ou 'full'
    
    Returns:
        Tuple de (eval_data, source_path) ou (None, None)
    """
    claude_path = ROOT / "prompts/web/claude" / target
    if claude_path.is_dir():
        eval_file = claude_path / "evals" / "evals.json"
        if eval_file.exists():
            with open(eval_file) as f:
                return json.load(f), claude_path

    chatgpt_eval_file = ROOT / "prompts/web/chatgpt/evals/evals.json"
    if chatgpt_eval_file.exists():
        with open(chatgpt_eval_file) as f:
            data = json.load(f)
            if target.lower() == "chatgpt":
                return data, chatgpt_eval_file.parent
            filtered = [e for e in data.get("evals", []) if e.get("skill") == target]
            if filtered:
                return {"skill_name": f"ChatGPT: {target}", "evals": filtered}, chatgpt_eval_file

    if target == "full":
        full_test = ROOT / "skills/lovel-tester/evals/full_test.json"
        if full_test.exists():
            with open(full_test) as f:
                return json.load(f), full_test.parent

    return None, None


def load_fixture(prompt: str) -> str:
    """
    Substitui {{fixture:name}} com o conteúdo do arquivo.
    
    Args:
        prompt: Prompt com referências a fixtures
    
    Returns:
        Prompt com fixtures substituídos
    """
    fixtures_dir = ROOT / "prompts/web/claude/tests/fixtures"
    matches = re.findall(r'\{\{fixture:(.*?)\}\}', prompt)
    for name in matches:
        for ext in [".md", ""]:
            fixture_file = fixtures_dir / (name + ext)
            if fixture_file.exists():
                with open(fixture_file) as f:
                    prompt = prompt.replace(f"{{{{fixture:{name}}}}}", f.read())
                break
    return prompt


def validate_deterministic(skill_name: str, output: str) -> Dict[str, Any]:
    """
    Valida output de forma determinística usando script Python.
    
    Este script é executado via subprocess e retorna JSON.
    O código do validator NUNCA entra no contexto - apenas o output.
    
    Args:
        skill_name: Nome da skill (hunting, outreach, post, parecer)
        output: Output da skill a ser validado
    
    Returns:
        Dict com valid, score, issues
    """
    try:
        result = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR_SCRIPT),
                "--skill", skill_name.lower(),
                "--output", output
            ],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            try:
                return json.loads(result.stdout.strip())
            except json.JSONDecodeError:
                return {
                    "valid": False,
                    "score": 0,
                    "issues": [f"Invalid JSON from validator: {result.stdout[:100]}"]
                }
        else:
            return {
                "valid": False,
                "score": 0,
                "issues": [f"Validator error: {result.stderr[:200]}"]
            }
    except subprocess.TimeoutExpired:
        return {
            "valid": False,
            "score": 0,
            "issues": ["Validator timeout"]
        }
    except Exception as e:
        return {
            "valid": False,
            "score": 0,
            "issues": [f"Validator exception: {str(e)}"]
        }


def calculate_consistency(outputs: List[str]) -> Dict[str, Any]:
    """
    Calcula consistência entre múltiplas execuções.
    
    Args:
        outputs: Lista de outputs
    
    Returns:
        Dict com score e status
    """
    if len(outputs) < 2:
        return {"score": 10.0, "status": "✅"}
    
    lens = [len(o) for o in outputs]
    std_dev = statistics.stdev(lens) if len(lens) > 1 else 0
    mean_len = statistics.mean(lens)
    coeff_var = (std_dev / mean_len) if mean_len > 0 else 0
    
    score = max(0, 10 * (1 - coeff_var))
    return {
        "score": round(score, 2),
        "status": "✅" if score > 8 else "⚠️" if score > 5 else "❌",
        "coeff_var": round(coeff_var, 3)
    }


def run_benchmark(target: str, iters: int = 1) -> None:
    """
    Executa benchmark completo de uma skill.
    
    Args:
        target: Nome da skill a testar
        iters: Número de execuções por eval
    """
    eval_data, source_path = find_evals(target)
    
    if not eval_data:
        print(f"❌ Target '{target}' não encontrado.")
        return

    skill_name = eval_data.get('skill_name', target)
    
    print(f"🎯 BENCHMARK: {skill_name}")
    print(f"   Source: {source_path} | Iterations: {iters}")
    print("-" * 50)

    llm_client.reset_stats()
    results: List[Dict] = []
    total_latency = 0

    for item in eval_data["evals"]:
        # Extract base skill name (remove "lovel-" prefix if present)
        item_skill_raw = item.get("skill", skill_name)
        item_skill = item_skill_raw.lower().replace("lovel-", "").replace(" Lovel", "").split()[0]
        
        raw_prompt = item["prompt"]
        final_prompt = load_fixture(raw_prompt)
        
        print(f"\n📋 Eval {item['id']}: {raw_prompt[:60]}...")
        
        run_outputs: List[str] = []
        item_tokens = 0
        item_latency = 0
        
        for i in range(iters):
            print(f"   [{i+1}/{iters}] Executing...", end="\r", flush=True)
            res = llm_client.call_llm(final_prompt)
            
            if res.get("error"):
                print(f"   ❌ Error: {res.get('error')}")
                sys.exit(1)
            
            run_outputs.append(res['output'])
            item_tokens += res['tokens']
            item_latency += res['latency']

        print(f"   ⚖️  Validating...", end="\r", flush=True)
        
        # Validação determinística
        validation = validate_deterministic(item_skill, run_outputs[-1])
        
        # Show issues for debugging
        if validation.get("issues"):
            print(f"   ⚠️  Issues: {validation['issues']}")
        
        consistency = calculate_consistency(run_outputs)

        result = {
            "id": item["id"],
            "passed": validation["valid"],
            "score": validation["score"],
            "issues": validation.get("issues", []),
            "tokens": item_tokens,
            "latency": item_latency,
            "consistency": consistency["score"]
        }
        results.append(result)
        total_latency += item_latency

        status = "✅" if result["passed"] else "❌"
        issues_str = f" | Issues: {len(result['issues'])}" if result['issues'] else ""
        print(f"   {status} {result['score']}/10{issues_str}")

    stats = llm_client.get_stats()
    passed_count = sum(1 for r in results if r["passed"])
    avg_score = statistics.mean([r["score"] for r in results])
    avg_cons = statistics.mean([r["consistency"] for r in results])

    print("\n" + "="*50)
    print(f"📊 BENCHMARK SUMMARY")
    print(f"   Pass Rate:   {passed_count}/{len(results)} ({(passed_count/len(results))*100:.1f}%)")
    print(f"   Avg Score:   {avg_score:.2f}/10")
    print(f"   Consistency: {avg_cons:.2f}/10")
    print(f"   Est. Tokens: ~{stats['total_tokens']:,}")
    print(f"   Est. Cost:   ~${stats['total_cost']:.4f}")
    print(f"   Avg Latency: {total_latency/len(results)/1000:.2f}s")
    print("="*50)


def main():
    """CLI entry point."""
    if len(sys.argv) < 2:
        print("Usage: python run_eval.py <skill> [iterations]")
        print("Skills: hunting, outreach, post, parecer")
        sys.exit(1)
    
    llm_client.configure(llm_eval="opencode", llm_grading="opencode")
    
    target = sys.argv[1]
    iters = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 1
    
    run_benchmark(target, iters)


if __name__ == "__main__":
    main()
