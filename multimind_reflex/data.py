from dataclasses import dataclass


@dataclass(frozen=True)
class Message:
    speaker: str
    role: str
    time: str
    text: str
    kind: str = "agent"


MESSAGES = [
    Message("You", "Direction", "09:12", "Build a decision brief that keeps the evidence trail visible." , "user"),
    Message("Research", "Evidence agent", "09:13", "I found three constraints: continuity, legibility under load, and a mutation path that does not discard session truth."),
    Message("Critic", "Counterpoint", "09:14", "Do not mistake a theme swap for morphology. The conversation must survive a real change in spatial grammar."),
    Message("Synthesis", "Orchestrator", "09:16", "Working thesis: preserve the thread as the stable object, then let each presentation reinterpret its surrounding instruments."),
    Message("Research", "Evidence agent", "09:18", "The long-session risk is attention fatigue. Status needs to be compact, while the thread remains airy and easy to scan."),
    Message("Critic", "Counterpoint", "09:19", "The mobile version cannot simply inherit the desktop rail. Give the thread the viewport and put agency controls into a deliberate dock."),
    Message("Synthesis", "Orchestrator", "09:21", "I am assembling the comparison. The active argument is stored as a shared session artifact, not as presentation state."),
    Message("Research", "Evidence agent", "09:23", "Evidence pass complete: interactions are available to the next agent without moving the reader away from the active exchange."),
    Message("Critic", "Counterpoint", "09:24", "Keep an explicit waiting state. Empty activity is ambiguous; structured waiting tells the operator what the system is doing."),
    Message("Synthesis", "Orchestrator", "09:26", "Draft ready. I have retained the dissent and marked the uncertainty in the decision log."),
]
AGENTS = [
    ("Research", "running", "Collecting source tension", "68%"),
    ("Critic", "waiting", "Watching the synthesis", "—"),
    ("Synthesis", "pending", "Composing decision brief", "42%"),
]
