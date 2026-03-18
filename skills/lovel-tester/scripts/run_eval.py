#!/usr/bin/env python3
"""
Lovel Eval Runner - OpenCode Only
Uses OpenCode (Claude) for both eval and grading.
"""

import json
import sys
import re
import statistics
from pathlib import Path

import llm_client

ROOT = Path(__file__).resolve().parent.parent.parent.parent
GRADER_FILE = ROOT / "skills/lovel-tester/agents/grader.md"


def find_evals(target: str) -> tuple:
    """Find evals based on target (skill name, platform, or 'full')."""
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
            if target.lower() == "chatgpt": return data, chatgpt_eval_file.parent
            filtered = [e for e in data.get("evals", []) if e.get("skill") == target]
            if filtered: return {"skill_name": f"ChatGPT: {target}", "evals": filtered}, chatgpt_eval_file

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

    grade_prompt = f"""Evaluate the following recruiting skill response:
---
Skill: {skill_name}
Input: {prompt}
Expected: {expected}
Actual Output: {actual}
---
Return only a JSON object: {{"passed": boolean, "score": 0-10, "final_verdict": "short reason"}}
"""
    result = llm_client.call_llm(grade_prompt, system_prompt=instructions, for_grading=True)
    response = result["output"]
    
    try:
        json_match = re.search(r'\{[\s\S]*\}', response)
        if json_match:
            data = json.loads(json_match.group())
            if "passed" in data and "score" in data:
                data.setdefault("final_verdict", data.get("evaluations", [{}])[0].get("evidence", "OK") if data.get("evaluations") else "Evaluated")
                return data
        return {"passed": False, "score": 0, "final_verdict": f"Invalid Grader JSON: {response[:100]}..."}
    except json.JSONDecodeError as e:
        return {"passed": False, "score": 0, "final_verdict": f"JSON parse error: {str(e)} | Response: {response[:100]}..."}
    except Exception as e:
        return {"passed": False, "score": 0, "final_verdict": f"Error: {str(e)}"}


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


def load_fixture(prompt: str) -> str:
    """Replace {{fixture:name}} with the content of the file in tests/fixtures/."""
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


def run_benchmark(target: str, iters: int = 1) -> None:
    """Run a full benchmark suite."""
    eval_data, source_path = find_evals(target)
    
    if not eval_data:
        print(f"❌ Target '{target}' not found.")
        return

    print(f"🎯 BENCHMARK: {eval_data.get('skill_name', target)}")
    print(f"   Source: {source_path} | Iterations: {iters}")
    print("-" * 50)

    llm_client.reset_stats()
    results = []
    total_latency = 0

    for item in eval_data["evals"]:
        skill_ctx = item.get("skill", eval_data.get("skill_name"))
        
        raw_prompt = item["prompt"]
        final_prompt = load_fixture(raw_prompt)
        
        print(f"\n📋 Eval {item['id']}: {raw_prompt[:60]}...")
        
        run_outputs = []
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

        print(f"   ⚖️  Grading...", end="\r", flush=True)
        grading = grade_response(skill_ctx, final_prompt, item['expected_output'], run_outputs[-1])
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
        total_latency += item_latency

        status = "✅" if result["passed"] else "❌"
        print(f"   {status} {result['score']}/10 | {result['verdict'][:60]}...")

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


if __name__ == "__main__":
    llm_client.configure(llm_eval="opencode", llm_grading="opencode")
    
    if len(sys.argv) < 2:
        print("Usage: python run_eval.py <target> [iterations]")
        sys.exit(1)
    
    target = sys.argv[1]
    iters = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 1
    
    run_benchmark(target, iters)
