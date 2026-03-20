---
description: Daemon workflow to monitor the IPC directory and execute Antigravity subagents for pending LLM requests
---

# Antigravity Subagent Daemon Workflow

This workflow instructs the Antigravity agent to act as a persistent background daemon, monitoring the local IPC requests queue created by `llm_client.py` and processing them one by one.

## How to use
Run this workflow continuously when executing pipelines that use `llm_eval="antigravity"`.

## Steps

1. Use the `list_dir` tool to check the contents of `/home/tg/Projetos/rh-carol/ipc/requests/`. 
2. If there are pending JSON files in the requests directory:
   - For each file, read it using `view_file` to extract the `system_prompt` and `prompt`.
   - If the task requires browsing the web or interacting with pages, spawn a `browser_subagent` using the `Task` prompt extracted from the JSON file.
   - If the task is purely logic, analysis, or text generation, process it directly using your agentic capabilities and KIs context.
   - Write the generated output to a new file in `/home/tg/Projetos/rh-carol/ipc/responses/{id}.json` matching the structure:
     ```json
     {
       "id": "requst-id",
       "status": "completed",
       "output": "<your detailed markdown/text response here>",
       "tokens": 0,
       "error": null
     }
     ```
   - Delete the request JSON file from `/home/tg/Projetos/rh-carol/ipc/requests/` to mark it as handled.
3. If there are no pending files, wait and check again, or prompt the user if they want you to keep waiting.
