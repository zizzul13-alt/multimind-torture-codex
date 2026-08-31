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

## FastHTML candidate — local run

This branch contains the independent FastHTML candidate. It deliberately uses
port **8037** to avoid the other benchmark candidates.

```powershell
python -m pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:8037/`. Run focused checks with `npm test`.

For evidence capture, take a desktop image after entering the session, then
use a 390 × 844 viewport and take the mobile image. In either viewport, scroll
the conversation away from the end, select SIGNAL then ATLAS, and confirm that
the same messages and conversation scroll offset remain. Click agent rows and
send a message to exercise live state and dynamic interaction.

See `BENCHMARK_EVIDENCE.md` for an honest cost and result assessment.
