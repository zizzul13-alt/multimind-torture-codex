# MultiMind Platform Torture Test

Isolated proof-of-concept repository for evaluating potential future
presentation platforms for MultiMind.

This repository is NOT the MultiMind production repository.

## Purpose

Evaluate candidate platforms against the same visual, interaction,
responsive, material, and engineering requirements.

Candidates:

- FastHTML
- Reflex
- SvelteKit + FastAPI

## Important

Do not use the existing MultiMind implementation as a visual shortcut.

The benchmark specification in `benchmark-brief.md` is the source of truth.

A candidate is not required to win.

`NO_MIGRATION_TARGET_APPROVED` is a valid final outcome.

## Reflex candidate

This track is a self-contained Reflex proof—not the MultiMind production
application. It uses a state-driven A/B presentation mutation, a realistic
mock debate session, a long conversation, and a purpose-built mobile
composition.

### Run locally

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
reflex init
reflex run --frontend-port 3092 --backend-port 8092
```

Visit `http://127.0.0.1:3092`. Reflex uses frontend port **3092** and backend
port **8092**, selected to avoid the parallel FastHTML and SvelteKit tracks.

Run focused checks with `pytest -q`. The repeatable browser sequence and the
architectural assessment are in [BENCHMARK_REPORT.md](BENCHMARK_REPORT.md) and
[evidence/VALIDATION.md](evidence/VALIDATION.md).
