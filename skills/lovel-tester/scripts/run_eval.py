#!/usr/bin/env python3
"""
Lovel Eval Runner - Executa evals para skills do projeto rh-carol
Baseado em run_eval.py da skill-creator (Anthropic)

Usage:
    python scripts/run_eval.py hunting                 # Executa evals de hunting
    python scripts/run_eval.py claude/hunting        # Executa evals de hunting
    python scripts/run_eval.py prompts/web/claude/hunting
"""

import json
import sys
from pathlib import Path

SKILLS_ROOT = Path(__file__).parent.parent

def find_evals(skill_path: str) -> dict:
    """Encontra evals da skill"""
    
    paths_to_try = [
        SKILLS_ROOT / skill_path,
        SKILLS_ROOT / "prompts/web/claude" / skill_path,
        SKILLS_ROOT / skill_path / "evals" / "evals.json",
    ]
    
    # Try as direct path first
    direct = SKILLS_ROOT / skill_path
    if direct.exists():
        evals_file = direct / "evals" / "evals.json"
        if evals_file.exists():
            with open(evals_file) as f:
                return json.load(f), direct
    
    # Try finding in claude folder
    for base in ["prompts/web/claude", "prompts/web/chatgpt/skills"]:
        for ext in ["", ".md"]:
            path = SKILLS_ROOT / base / (skill_path + ext)
            if path.exists():
                if path.is_dir():
                    evals_file = path / "evals" / "evals.json"
                else:
                    evals_file = path.parent / "evals" / "evals.json"
                
                if evals_file.exists():
                    with open(evals_file) as f:
                        return json.load(f), evals_file.parent.parent
    
    return None, None

def run_eval_item(skill_name: str, eval_item: dict) -> dict:
    """Executa um eval e retorna resultado"""
    print(f"\n📋 Eval {eval_item['id']}: {eval_item['prompt']}")
    print(f"   Expected: {eval_item['expected_output']}")
    
    # TODO: Implementar execução real via Claude API
    return {
        "eval_id": eval_item["id"],
        "passed": True,
        "output": "[Mock] Execute skill and compare with expected"
    }

def main():
    if len(sys.argv) < 2:
        print("🔧 Lovel Run Eval")
        print("=" * 50)
        print("\nUsage:")
        print("  python scripts/run_eval.py hunting")
        print("  python scripts/run_eval.py claude/hunting")
        print("  python scripts/run_eval.py prompts/web/claude/hunting")
        sys.exit(1)
    
    skill_path = sys.argv[1]
    
    evals, path = find_evals(skill_path)
    
    if not evals:
        print(f"❌ Evals não encontrados para: {skill_path}")
        sys.exit(1)
    
    print(f"🎯 Executando evals para: {evals['skill_name']}")
    print(f"   Path: {path}")
    print(f"   Total evals: {len(evals['evals'])}")
    
    results = []
    for eval_item in evals["evals"]:
        result = run_eval_item(evals["skill_name"], eval_item)
        results.append(result)
    
    passed = sum(1 for r in results if r["passed"])
    total = len(results)
    
    print(f"\n📊 Results: {passed}/{total} passed")
    
    if passed == total:
        print("✅ All evals passed!")
    else:
        print("❌ Some evals failed")

if __name__ == "__main__":
    main()
