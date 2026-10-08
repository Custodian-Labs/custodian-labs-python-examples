# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

Public, beginner-facing example scripts for the `custodian-labs` Python SDK (PyPI). No library code, tests or build system — only runnable samples. The SDK source lives in the sibling repo `../custodian-python-sdk`; check it for the real API before changing an example.

GitHub: `Custodian-Labs/custodian-labs-python`. Community contributions come in via fork → PR into `application_examples/` (see `application_examples/README.md` and `.github/pull_request_template.md`).

## Layout

| Path | Contents |
|---|---|
| `01_AI_agent_RAG.py` → `04_multi_agent_team_routing.py` | Numbered learning path: RAG, few-shot, builder chain, multi-agent routing (`single` / `workflow` / `chain`) |
| `application_examples/` | Real-world agents, named by use case (no numbers) + `_template.py` for contributors |
| `guardian_layer_examples/` | `GuardianLayer` PII masking: text (`01_`) and file (`02_`) |
| `websocket_examples/` | FastAPI WebSocket bridge (`01_`) + browser client (`02_`) |
| `data_examples/` | Fictional sample data: `car_info.csv`, `pii_data.csv`, `contract.pdf`, `CV.docx` |

Each subfolder has its own `01_`, `02_` numbering.

## Running

```bash
pip install custodian-labs
cp .env.example .env                            # add CUSTODIAN_SDK_API_KEY (SDK 0.2.4+ reads .env; or export it)
python 01_AI_agent_RAG.py                       # always run from the repo root
python application_examples/cv_recruiter_assistant.py
```

Data paths are plain relative strings (`"data_examples/car_info.csv"`), so scripts must be run from the repo root. Only the WebSocket bridge needs extra packages; they're listed in a comment at the top of that file (`fastapi`, `"uvicorn[standard]"`). There is no `requirements.txt` on purpose.

## Conventions for Examples

Examples are for beginners. Keep each one a single, self-contained file that matches the existing style:

- **Plan note at the top.** Agent examples: Free = 1 deployed Custodian, always `gpt-4o`; Pro = more Custodians and models. Multi-agent examples start with `REQUIRES A PRO PLAN`. GuardianLayer examples get a usage-credits note instead.
- Current SDK names only: `Custodian`, `CustodianBuilder`, `CustodianSquad`, `GuardianLayer`. Never `Assistant`, `AssistantBuilder`, `Agent`, `AgentTeam` (deprecated aliases) or `create_assistant` (removed).
- Variable name `ai_agent`; always pass `name=`; print `app.chat_url` after `deploy()`, followed by `# To remove this deployment later, delete it under My AIs in the Dashboard.` (the SDK has no delete method).
- `reply = app.chat("...")` then `print(reply.response)` — no `if reply is not None:` guard. `app.chat()` with no argument starts an interactive CLI chat.
- Model-override tips use `model="gpt-4o-mini"` and say Pro only. Don't use `claude-3.5-sonnet` (retired).
- Short comments that explain *why*; link docs at `https://docs.custodianlabs.io/python-sdk/...`.
- Sample data must be fictional (`example.com` emails, `555` numbers). No API keys in code.
- Web search tools and Gmail are documented on the docs site, not shown here.

## Platform Behavior Worth Knowing

- Free plan: max 1 deployed chatbot; any `model=` is silently replaced with `gpt-4o`. Every deploy creates a new deployment, so scripts that deploy in a loop or on each request burn through the limit.
- Multi-agent `single` routing is keyword matching: each topic word found in the message scores +5, the agent name +6, ties go to the first agent listed. Choose example questions so the intended agent wins.
- `reply.handoff_path` lists the agents involved in every routing mode; `reply.selected_agent` is the first.
- `privacy_enabled=True` masks names, phones, ages and dates before the LLM and restores them in the reply.

## README

`README.md` has a "How It Works" section with one Mermaid diagram (GitHub renders it). Update the samples tables when adding, renaming or removing an example. Validate diagram changes at https://mermaid.live.
