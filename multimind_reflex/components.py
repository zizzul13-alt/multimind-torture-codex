import reflex as rx

from .data import AGENTS, MESSAGES
from .state import BenchmarkState


def wordmark() -> rx.Component:
    return rx.el.div(
        rx.el.span("MULTI", class_name="wordmark-main"),
        rx.el.span("MIND", class_name="wordmark-accent"),
        rx.el.span("/ operational intelligence", class_name="wordmark-sub"),
        class_name="wordmark",
    )


def status_dot(status: str) -> rx.Component:
    return rx.el.span(class_name=f"status-dot {status}", aria_label=status)


def agent_row(agent: tuple[str, str, str, str]) -> rx.Component:
    name, status, note, progress = agent
    return rx.el.button(
        rx.el.span(status_dot(status), rx.el.span(name, class_name="agent-name"), class_name="agent-title"),
        rx.el.span(note, class_name="agent-note"),
        rx.el.span(progress, class_name="agent-progress"),
        class_name="agent-row",
        data_agent=name,
        on_click=BenchmarkState.choose_agent(name),
    )


def agent_constellation() -> rx.Component:
    return rx.el.section(
        rx.el.div(rx.el.span("LIVE DEBATE", class_name="eyebrow"), rx.el.span("03", class_name="count"), class_name="section-kicker"),
        rx.el.div(*[agent_row(agent) for agent in AGENTS], class_name="agent-list"),
        rx.el.div(
            rx.el.span("Shared premise", class_name="mini-label"),
            rx.el.p("A session is a durable argument: evidence, dissent, and direction remain available across every presentation.", class_name="premise"),
            class_name="premise-block",
        ),
        class_name="agent-constellation panel",
    )


def message_item(message) -> rx.Component:
    return rx.el.article(
        rx.el.div(
            rx.el.span(message.speaker, class_name="message-speaker"),
            rx.el.span(message.role, class_name="message-role"),
            rx.el.time(message.time, class_name="message-time"),
            class_name="message-meta",
        ),
        rx.el.p(message.text, class_name="message-copy"),
        class_name=f"message message-{message.kind}",
    )


def conversation() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(rx.el.span("SESSION 04", class_name="eyebrow"), rx.el.h1("The architecture argument", class_name="thread-title")),
            rx.el.div(rx.el.span("LONG THREAD", class_name="thread-counter"), rx.el.span(BenchmarkState.message_count, class_name="thread-number"), class_name="thread-stat"),
            class_name="thread-header",
        ),
        rx.el.div(*[message_item(message) for message in MESSAGES], class_name="message-stream", id="conversation-scroll", data_scroll_region="conversation"),
        rx.el.div(
            rx.el.button("Add session marker", on_click=BenchmarkState.add_note, class_name="quiet-action"),
            rx.el.span("Session truth persists through presentation changes.", class_name="persistence-note"),
            class_name="thread-footer",
        ),
        class_name="conversation panel",
    )


def decision_strip() -> rx.Component:
    return rx.el.section(
        rx.el.div(rx.el.span("SYNTHESIS", class_name="eyebrow"), rx.el.h2("Continuity is the feature.", class_name="decision-title")),
        rx.el.p("Reflex coordinates the visible exchange from Python state while this CSS layer supplies two separate visual grammars.", class_name="decision-copy"),
        rx.el.div(rx.el.span("EVIDENCE", class_name="signal-label"), rx.el.span("09 artifacts", class_name="signal-value"), class_name="signal-line"),
        rx.el.div(rx.el.span("CONFIDENCE", class_name="signal-label"), rx.el.span("0.82", class_name="signal-value"), class_name="signal-line"),
        class_name="decision-strip panel",
    )


def mobile_dock() -> rx.Component:
    return rx.el.nav(
        rx.el.button("Thread", class_name="dock-item active"),
        rx.el.button("Agents", class_name="dock-item"),
        rx.el.button("Brief", class_name="dock-item"),
        rx.el.button("Command", on_click=BenchmarkState.toggle_command, class_name="dock-item command"),
        class_name="mobile-dock",
        aria_label="Mobile session navigation",
    )


def command_sheet() -> rx.Component:
    return rx.cond(
        BenchmarkState.command_open,
        rx.el.div(
            rx.el.button("Close", on_click=BenchmarkState.toggle_command, class_name="sheet-close"),
            rx.el.span("SESSION COMMANDS", class_name="eyebrow"),
            rx.el.button("Focus Research", on_click=BenchmarkState.choose_agent("Research"), class_name="sheet-command"),
            rx.el.button("Add session marker", on_click=BenchmarkState.add_note, class_name="sheet-command"),
            class_name="command-sheet",
        ),
    )
