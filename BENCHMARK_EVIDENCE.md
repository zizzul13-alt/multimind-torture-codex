# FastHTML benchmark evidence

## Reproduction

- Start: `python -m pip install -r requirements.txt; python app.py`
- URL / port: `http://127.0.0.1:8037/` (8037)
- Tests: `npm test`
- Manual dynamic proof: open the session, scroll its conversation, select
  SIGNAL, then ATLAS. The JS retains the `session` object and restores the
  conversation element's captured `scrollTop` in `requestAnimationFrame`.

## Implemented proof

The opening is a material-first scroll scene using a self-contained SVG
aurora, layered color fields, clipped radial/rule materials, and two
scroll-linked planes. Its four reference slices are deliberately distinct:
Arknights (weather/layering), Noomo (pointer-reactive axis), Dioriviera
(restraint/material), and Viens-la (type/rules).

The MultiMind proof supplies a mock user, 16 long-form debate messages,
three stateful agents, message entry, loading-state pulse, sticky conversation
controls, and two visual constructions:

- **Atlas:** porous, pale, editorial conversation with sparse side memory.
- **Signal:** dark segmented field, ruled transcript, hard agent surface and
  dense terminal geometry.

Mobile at 390 × 844 hides desktop rails, promotes a compact agent header,
uses a full-screen conversation, and adds a fixed bottom command surface.
It is not a stacked desktop grid. Reduced-motion is supported.

## Test and runtime record

- `npm test`: 5/5 passed (route/material contract, four proof markers,
  no-navigation mode mutation plus scroll capture, dedicated mobile branch,
  long conversation/input/reduced-motion path).
- HTTP smoke test: `GET /` returned 200 from a temporary Python 3.12 runtime
  with `python-fasthtml 0.14.12` on port 8037.
- Browser capture: the provided in-app browser connector returned “No browser
  is available”; no screenshots were claimed or manufactured. The README gives
  deterministic capture instructions.

## Cost accounting

| Measure | Count / assessment |
| --- | --- |
| Authored application Python | 18 LOC (intentionally compact) |
| CSS | 8 physical LOC / ~5.2k characters (minified deliberately for this PoC) |
| Authored browser JS | 4 physical LOC / ~4.0k characters (minified deliberately) |
| Test code | 2 physical LOC / 5 focused tests |
| Custom raw HTML | One `NotStr` vertical-slice body, ~3.8k characters |
| Custom JS | One state/render/mutation module, ~4.0k characters |
| FastHTML escape hatches | Raw HTML body and browser JS; no DOM-selector dependency on framework internals |
| Significant dependencies | python-fasthtml and its Starlette/Uvicorn transitives; Node built-in test runner |

FastHTML's intended HTML/CSS/browser-JS idiom makes the CSS and browser JS
native in philosophy, but the large raw HTML string is a real ergonomics cost:
it avoids a component forest at the price of authoring comfort and compile-time
structure. No custom animation engine was used; the SVG material and CSS layers
carry most of the visual work.

## Assessment

| Dimension | Result |
| --- | --- |
| Reference parity | MINIMUM_PASS (capability slice, not copied sites) |
| Live A → B → A | Implemented without page navigation; session and scroll retained |
| Long conversation | Implemented, readable transcript with sticky composer |
| Mobile recomposition | Implemented as full-screen conversation + bottom commands |
| Framework fingerprint | No default component-library signature; custom CSS dominates |
| Abstraction survival | **78%** — HTML/CSS/JS are FastHTML-native, but raw HTML is a notable cost |
| Benchmark classification | **MINIMUM_PASS** |
| Final verdict vocabulary | **GOOD** |

This does not approve FastHTML as a migration target. Its visual ceiling is
demonstrated, while the raw-markup / custom-client-code cost remains material.
