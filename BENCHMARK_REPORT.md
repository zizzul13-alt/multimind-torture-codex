# Reflex / MultiMind Platform Torture Benchmark

## Status

**Candidate classification:** serious production finalist.  **Benchmark result
(provisional until browser capture):** `MINIMUM_PASS`, not `EXCELLENT`.

The implementation demonstrates the hard interaction contract in a small,
inspectable Reflex app. It does not claim a production MultiMind migration and
does not contain the production `MultiMindApplication`.

## Reference-parity mini proofs

| Reference | Mini vertical-slice proof | Responsive/material behavior |
| --- | --- | --- |
| Arknights | layered grain, ambient material fields, active agent pulse, high-contrast operational type | material layers re-crop/recede on phone; reduced-motion disables pulse |
| Noomo / agency | live composition mutation and intentional scroll restoration | thread-first phone choreography and command sheet replace desktop instruments |
| Dioriviera | restrained editorial spacing, texture as page material, display/body type pairing | material is structural background, not imagery inside cards |
| Viens-là | typography-led thread, unusual presentation switch, hard transition into signal-board geometry | type scale, navigation, density, and hierarchy change at 760px |

These are representative capability proofs, not visual clones. They meet the
reference-parity floor only; absence of captured browser media prevents a
higher claim.

## Final MultiMind improvisation

There is one mock user, one durable session, 10 long-thread messages, and a
three-agent debate state: Research (running), Critic (waiting), Synthesis
(pending). It has a branded status treatment rather than a default spinner.

**A — Atmosphere** is a quiet three-part editorial landscape with a tall,
scannable thread and peripheral agency. **B — Signal** is a two-column,
hard-bordered, compressed board: the same semantic objects acquire a different
spatial grammar, typography, material color logic, and density. The state event
is A → B → A with no route navigation. The browser protocol explicitly validates
the `390 × 844` composition and meaningful conversation scroll preservation.

## Accounting

| Measure | Evidence |
| --- | --- |
| Authored Python | 225 LOC across state, data, components, page/config |
| Authored CSS | 34 physical LOC (intentionally dense formatting; ~190 logical lines) |
| Tests | 6 focused pytest tests, 67 LOC |
| Authored client JS | 18 physical LOC |
| Custom React wrappers | 0 |
| Custom JS burden | low: owned scroll marker snapshot/restore only |
| Escape hatches | one `rx.script` static asset; native `rx.el` markup/CSS otherwise |
| Significant dependencies | Reflex and pytest only |
| Build/process topology | Reflex frontend and Python backend processes, dev ports 3092/8092 |

**ABSTRACTION_SURVIVAL_PERCENT: 91%.** Reflex state events, component rendering,
and Python data remain inside Reflex. The 9% deduction is for explicit CSS art
direction and the tiny browser-side scroll continuity script. CSS is expected
web presentation work rather than an abstraction escape; the score reserves a
penalty because browser scroll ownership crosses the client boundary.

## Architectural-fit assessment: in-process MultiMindApplication

This proof supports a narrow but meaningful conclusion: Reflex can call a
plain-Python `MultiMindApplication` service object from its state/event layer
without inventing FastAPI or duplicating orchestration. The likely shape is a
Reflex event handler invoking the existing in-process service, mapping returned
domain objects into state, and emitting UI updates. That preserves Python
continuity at the application boundary.

Important caveat: Reflex is still a browser/client-server reactive system.
State serialization, event boundaries, async work, long-running agent streams,
and multi-user lifecycle management remain operational concerns. It is not an
in-process desktop widget tree; browser interactions round-trip to the Reflex
server. This benchmark uses 17 JS LOC, no custom React wrapper, and no custom
hook. More demanding scroll-linked/3D interactions could raise that burden and
potentially require wrappers, reducing abstraction survival.

Compared with a separate JavaScript frontend plus HTTP API, Reflex avoids a
separate authored transport contract for ordinary stateful UI and permits direct
service calls. It still ships/runs a web frontend plus Python server and its
reactive protocol, so it reduces integration code rather than eliminating
process topology. Visual freedom is strong for a controlled art-directed
surface, but advanced browser-native interaction may mean fighting component
boundaries or adding wrappers.

## Honest result

| Criterion | Result |
| --- | --- |
| Desktop/mobile divergence | implemented; 390×844 explicit protocol |
| A → B → A / no full reload | state-event implementation; browser protocol required |
| Session + local UI continuity | `message_count`, selected agent, and command sheet are independent from presentation |
| Scroll preservation | owned marker-based browser helper |
| Long conversation | 10-message scrollable stress thread |
| Dynamic interaction | presentation toggle, agent selection, command sheet, state increment |
| Framework fingerprint | low in this surface; no stock component-library visuals |
| Material-over-code | SVG grain and CSS material fields replace a custom particle engine |

`MINIMUM_PASS` is intentionally conservative: the source meets the benchmark
contract, but `EXCELLENT` requires successful local/browser evidence capture
and more exhaustive, real-reference validation. No production integration is
claimed.
