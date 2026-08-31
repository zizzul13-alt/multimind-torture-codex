# Reflex benchmark validation protocol

## Local process and ports

Use a virtual environment and run from this repository:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
reflex init
reflex run --frontend-port 3092 --backend-port 8092
```

Open `http://127.0.0.1:3092`. These fixed local ports are intentionally
separate from the other candidate tracks: Reflex frontend `3092`, Reflex
backend `8092`.

## Browser evidence sequence

1. Capture the default desktop view at 1440px wide: this is morphology A,
   *Atmosphere*.
2. Scroll the conversation region until “Draft ready” is visible. Capture it.
3. Click **Atmosphere**. Confirm the page does not navigate or reload, the
   heading/messages are still present, and the thread remains at the same
   message. Capture morphology B, *Signal*.
4. Click **Signal** to return to morphology A. The message count and selected
   session remain live; repeat the scroll check.
5. At `390 × 844`, verify the agent and decision desktop panels are removed,
   the thread is viewport-first, and the persistent bottom dock has Thread,
   Agents, Brief, and Command. Open Command and capture its sheet.
6. Use **Add session marker**, switch morphology, and confirm the incremented
   long-thread count remains after the mutation.
7. Turn on `prefers-reduced-motion` and verify the running agent dot and
   transitions become still.

## Dynamic evidence criteria

The only authored client JavaScript is `assets/scroll-preservation.js` (17
non-blank LOC). It listens to this benchmark's own `data-morph-switch` and
`data-scroll-region` markers, snapshots `scrollTop` before mutation, and
restores it after the reactive DOM update. It has no knowledge of Reflex DOM
internals and does not implement application orchestration.

The A → B → A switch calls a Reflex state event, not a route or browser
navigation. Conversation content and message count live in Python state/data
and are independent of `presentation`.
