#!/usr/bin/env python3
"""
LLM Client Module - OpenCode (Claude) only for eval/grading.
"""

import time
import os
import requests
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent.parent

_env_file = ROOT / ".env"
if _env_file.exists():
    with open(_env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                os.environ[key.strip()] = value.strip()

_config: dict = {
    "llm_eval": "opencode",
    "llm_grading": "opencode",
    "session_id": None,
    "total_tokens": 0,
    "total_cost": 0.0,
}

COST_PER_1M_TOKENS: float = 3.0  # Claude 3.7 Sonnet


def get_stats() -> dict:
    """Return accumulated stats."""
    return {
        "total_tokens": _config["total_tokens"],
        "total_cost": _config["total_cost"],
    }


def reset_stats() -> None:
    """Reset accumulated stats."""
    _config["total_tokens"] = 0
    _config["total_cost"] = 0.0


def configure(llm_eval: str = "opencode", llm_grading: str = "opencode") -> None:
    """Configure the LLM backends (default: OpenCode for both)."""
    _config["llm_eval"] = llm_eval
    _config["llm_grading"] = llm_grading


def call_llm(prompt: str, system_prompt: str = "", for_grading: bool = False) -> dict:
    """Execute LLM call via OpenCode."""
    result = _call_llm_opencode(prompt, system_prompt)
    
    if result.get("output"):
        estimated_tokens = len(result["output"]) // 4
        result["tokens"] = estimated_tokens
        _config["total_tokens"] += estimated_tokens
        _config["total_cost"] += (estimated_tokens / 1_000_000) * COST_PER_1M_TOKENS
    
    return result


def _get_opencode_session() -> str:
    """Get or create an OpenCode session."""
    if _config.get("session_id") is None:
        resp = requests.post(
            "http://127.0.0.1:4096/session",
            json={"title": "llm-client"},
            timeout=10
        )
        _config["session_id"] = resp.json()["id"]
    return _config["session_id"]


def _call_llm_opencode(prompt: str, system_prompt: str = "") -> dict:
    """Execute LLM call via OpenCode REST API."""
    full_prompt = (
        f"{system_prompt}\n\nUser: {prompt}\n\nResponse:"
        if system_prompt else prompt
    )
    try:
        t0 = time.time()
        session_id = _get_opencode_session()
        
        message_resp = requests.post(
            f"http://127.0.0.1:4096/session/{session_id}/message",
            json={"parts": [{"type": "text", "text": full_prompt}]},
            timeout=120
        )
        
        latency = int((time.time() - t0) * 1000)
        
        if message_resp.status_code != 200:
            return {"error": message_resp.text, "output": "", "tokens": 0, "latency": latency}
        
        parts = message_resp.json().get("parts", [])
        output = ""
        for part in parts:
            if part.get("type") == "text":
                output = part.get("text", "")
                break
        
        return {"output": output.strip(), "tokens": 0, "latency": latency, "error": None}
    except requests.exceptions.ConnectionError:
        return {"error": "OPENCODE_SERVER_NOT_RUNNING", "output": "", "tokens": 0, "latency": 0}
    except Exception as e:
        return {"error": str(e), "output": "", "tokens": 0, "latency": 0}
