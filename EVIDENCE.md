# SvelteKit + FastAPI benchmark evidence

## Runbook

Frontend: `npm install && npm run dev` → `http://127.0.0.1:4173`.

Backend: `py -3 -m pip install -r requirements.txt && py -3 -m uvicorn backend.main:app --host 127.0.0.1 --port 8011` → `http://127.0.0.1:8011/health` (use `python` instead of `py -3` where it is the installed launcher).

Ports are deliberately isolated from the other candidate tracks: **4173** frontend and **8011** FastAPI.

## Reproducible browser checks

1. Open desktop viewport. Scroll the deliberation pane until message 05 is visible.
2. Select **B SIGNAL**, then **A ATLAS**. The message, session id, selected debate state, and pane scroll position remain; no navigation/reload occurs.
3. At **390 × 844**, the rail is replaced by a bottom command bar, compact project header, horizontally flowing agent strip, and conversation-first hierarchy. This is not desktop columns stacked vertically.
4. Click **READING MODE**, scroll, and use the mobile live action. The agent waiting material remains animated but quiet.
5. Request `GET /health` and `GET /api/session`; these demonstrate the actual FastAPI process and CORS-bound transport seam.

## Reference mini-slice mapping

| Reference | Proof in this slice |
| --- | --- |
| Arknights | Layered sun/material field, orbital agent activity, textured ambient plane, responsive art direction |
| Noomo / agency | Scrollable narrative scene, live morphology transition, non-standard data composition |
| Dioriviera | Large editorial negative space, material as structural backdrop, restrained palette and typography |
| Viens-là | Type-led hero, serial message indices, unusual compact navigation and poster-mode layout |

Reference parity is a capability floor, not a claim of full-site reproduction.

## Honest assessment

**Classification: EXCELLENT (benchmark slice only).** The candidate demonstrates browser-native material composition, a conversation surface that remains readable, and two genuinely different Svelte morphologies without replacing the semantic session. It is not `MAGNUM_OPUS`: the reference slices are compressed into one coherent proof and runtime metrics are modest rather than production-load tested.

**Abstraction survival: 92%.** Svelte components, scoped state, CSS, browser scrolling, and `fetch` are all idiomatic. The 8% escape hatch is direct browser `scrollTop` restoration and one native `requestAnimationFrame`; neither relies on undocumented DOM selectors or custom wrappers.

**FastAPI usage.** FastAPI owns health and a typed `/api/session` seam with CORS restricted to the local frontend origin. It is intentionally not a fake migration claim or a duplicated MultiMind orchestrator.

**Architecture cost.** This buys presentation freedom because Svelte owns the full browser render tree and CSS motion/material system. The cost is real: TypeScript/Svelte plus Python, Node plus Python environments, JSON serialization, CORS, two test systems, process coordination, network failure fallback, deployment topology, API versioning, and maintaining the transport contract. The UI retains a truthful rendered fallback if the local seam is unavailable, which keeps the benchmark interaction deterministic but must not be mistaken for offline production synchronization.

**Material-over-code.** The grain and shape materials are CSS/SVG compositing rather than a particle engine; only the stateful orbital/pulse indicators use lightweight CSS animation. No paid packages or component kits are used.

**Framework-cost notes.** Dependencies are Vite/Svelte/TypeScript test tooling on the frontend and FastAPI/Uvicorn/Pydantic/Pytest on the backend. There are no UI-library wrappers, no raw DOM selector hacking, and no full-page navigation for the presentation switch.

## Metrics

Measured on 2026-08-31 with `vite build` (generated output excluded from LOC):

| Measure | Evidence |
| --- | --- |
| Authored frontend TypeScript/Svelte LOC | 100 (93 component + 6 bootstrap + 1 type reference) |
| Authored backend Python LOC | 41 (27 service + 14 tests) |
| Authored CSS LOC | 5 physical dense CSS lines / 11,883 bytes; intentionally hand-authored, no generated CSS |
| Frontend tests | 2 Vitest assertions, passed |
| Backend tests | 2 Pytest tests, passed |
| Production JavaScript | 46,337 bytes / 18.30 kB gzip |
| Production CSS | 11,883 bytes / 3.61 kB gzip |
| Production total transfer | 58,387 bytes for HTML + JS + CSS (uncompressed); no binary media payload |
| Production requests | 3 first-party static files (HTML, one CSS, one JS); plus one session API request |
| JavaScript chunks | 1 |
| Static authored DOM elements | 84 template elements before repeated messages / agent data |
| Build result | 110 transformed modules; completed in 6.95 s |
| Runtime / hydration observation | Svelte mounts a single 46.3 kB browser bundle; direct browser instrumentation unavailable in this runner |
| Long-conversation / mobile observation | 8 realistic messages and dedicated 390 × 844 rules are implemented; browser screenshot/interactivity capture was unavailable because no browser target was attached to this session |

The external Google Font request is deliberately not included in the local static transfer total. It is a network/runtime cost to remove or self-host in a production assessment.
