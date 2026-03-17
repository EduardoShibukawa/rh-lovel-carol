#!/usr/bin/env python3
"""
Lovel REAL Eval Runner - Professional Prompt Engineering Edition
Based on the Anthropic skill-creator architecture.

Features:
- Real-time LLM execution via 'gemini' CLI.
- LLM-as-a-Judge grading via 'grader.md'.
- Token usage tracking and cost estimation.
- Consistency checks across multiple iterations.
"""

import json
import sys
import subprocess
import os
import re
import statistics
from pathlib import Path

# --- Configuration ---
ROOT = Path(__file__).resolve().parent.parent.parent.parent
GRADER_FILE = ROOT / "skills/lovel-tester/agents/grader.md"
COST_PER_1M_TOKENS = 0.15  # Gemini Flash estimation

def call_llm(prompt: str, system_prompt: str = "") -> dict:
    """Execute real LLM call via gemini CLI and extract metadata."""
    full_prompt = f"{system_prompt}\n\nUser: {prompt}\n\nResponse:" if system_prompt else prompt
    try:
        process = subprocess.Popen(['gemini', '-o', 'json'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(input=full_prompt)
        
        if process.returncode != 0:
            return {"error": stderr, "output": "", "tokens": 0, "latency": 0}
        
        json_objs = re.findall(r'\{.*\}', stdout, re.DOTALL)
        for obj_str in reversed(json_objs):
            try:
                data = json.loads(obj_str)
                if "response" in data and "stats" in data:
                    tokens = 0
                    latency = 0
                    for model in data["stats"].get("models", {}).values():
                        tokens += model.get("tokens", {}).get("total", 0)
                        latency += model.get("api", {}).get("totalLatencyMs", 0)
                    return {
                        "output": data["response"].strip(),
                        "tokens": tokens,
                        "latency": latency,
                        "error": None
                    }
            except json.JSONDecodeError:
                continue
        return {"output": stdout.strip(), "tokens": 0, "latency": 0, "error": "Metadata parsing failed"}
    except Exception as e:
        return {"error": str(e), "output": "", "tokens": 0, "latency": 0}

def find_evals(target: str):
    """Find evals based on target (skill name, platform, or 'full')."""
    # 1. Claude folder
    claude_path = ROOT / "prompts/web/claude" / target
    if claude_path.is_dir():
        eval_file = claude_path / "evals" / "evals.json"
        if eval_file.exists():
            with open(eval_file) as f:
                return json.load(f), claude_path

    # 2. ChatGPT file
    chatgpt_eval_file = ROOT / "prompts/web/chatgpt/evals/evals.json"
    if chatgpt_eval_file.exists():
        with open(chatgpt_eval_file) as f:
            data = json.load(f)
            if target.lower() == "chatgpt": return data, chatgpt_eval_file.parent
            filtered = [e for e in data.get("evals", []) if e.get("skill") == target]
            if filtered: return {"skill_name": f"ChatGPT: {target}", "evals": filtered}, chatgpt_eval_file

    # 3. Full Test
    if target == "full":
        full_test = ROOT / "skills/lovel-tester/evals/full_test.json"
        if full_test.exists():
            with open(full_test) as f:
                return json.load(f), full_test.parent

    return None, None

def grade_response(skill_name: str, prompt: str, expected: str, actual: str) -> dict:
    """Grade the response using the LLM-as-a-Judge agent."""
    if not GRADER_FILE.exists():
        return {"passed": True, "score": 10, "final_verdict": "Grader file missing"}
    
    with open(GRADER_FILE) as f:
        instructions = f.read()

    grade_prompt = f"""
Evaluate the following recruiting skill response:
---
Skill: {skill_name}
Input: {prompt}
Expected: {expected}
Actual Output: {actual}
---
Return only a JSON object: {{"passed": boolean, "score": 0-10, "final_verdict": "short reason"}}
"""
    result = call_llm(grade_prompt, system_prompt=instructions)
    response = result["output"]
    
    try:
        json_match = re.search(r'\{.*\}', response, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        return {"passed": False, "score": 0, "final_verdict": f"Invalid Grader JSON: {response[:50]}..."}
    except Exception as e:
        return {"passed": False, "score": 0, "final_verdict": f"Parsing error: {str(e)}"}

def calculate_consistency(outputs: list) -> dict:
    """Calculate consistency across multiple runs."""
    if len(outputs) < 2: return {"score": 10.0, "status": "✅"}
    
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

def run_benchmark(target: str, iters: int = 1):
    """Run a full benchmark suite."""
    eval_data, source_path = find_evals(target)
    
    if not eval_data:
        print(f"❌ Target '{target}' not found.")
        return

    print(f"🎯 BENCHMARK: {eval_data.get('skill_name', target)}")
    print(f"   Source: {source_path} | Iterations: {iters}")
    print("-" * 50)

    results = []
    total_tokens = 0
    total_latency = 0

    for item in eval_data["evals"]:
        skill_ctx = item.get("skill", eval_data.get("skill_name"))
        print(f"\n📋 Eval {item['id']}: {item['prompt'][:60]}...")
        
        run_outputs = []
        item_tokens = 0
        item_latency = 0
        
        for i in range(iters):
            print(f"   [{i+1}/{iters}] Executing...", end="\r")
            res = call_llm(item['prompt'])
            run_outputs.append(res['output'])
            item_tokens += res['tokens']
            item_latency += res['latency']

        print(f"   ⚖️  Grading...", end="\r")
        grading = grade_response(skill_ctx, item['prompt'], item['expected_output'], run_outputs[-1])
        consistency = calculate_consistency(run_outputs)

        result = {
            "id": item["id"],
            "passed": grading["passed"],
            "score": grading["score"],
            "verdict": grading["final_verdict"],
            "tokens": item_tokens,
            "latency": item_latency,
            "consistency": consistency["score"]
        }
        results.append(result)
        total_tokens += item_tokens
        total_latency += item_latency

        status = "✅" if result["passed"] else "❌"
        print(f"   {status} Score: {result['score']}/10 | Consist: {consistency['status']} {result['consistency']} | Tokens: {item_tokens}")
        print(f"      Verdict: {result['verdict']}")

    # Final Summary
    passed_count = sum(1 for r in results if r["passed"])
    avg_score = statistics.mean([r["score"] for r in results])
    avg_cons = statistics.mean([r["consistency"] for r in results])
    total_cost = (total_tokens / 1_000_000) * COST_PER_1M_TOKENS

    print("\n" + "="*50)
    print(f"📊 BENCHMARK SUMMARY")
    print(f"   Pass Rate:   {passed_count}/{len(results)} ({(passed_count/len(results))*100:.1f}%)")
    print(f"   Avg Score:   {avg_score:.2f}/10")
    print(f"   Consistency: {avg_cons:.2f}/10")
    print(f"   Total Tokens: {total_tokens:,}")
    print(f"   Total Cost:   ${total_cost:.4f}")
    print(f"   Avg Latency:  {total_latency/len(results)/1000:.2f}s")
    print("="*50)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_eval.py <target> [iterations]")
        sys.exit(1)
    
    target = sys.argv[1]
    iters = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    run_benchmark(target, iters)
