import reflex as rx

from .data import AGENTS, MESSAGES


class BenchmarkState(rx.State):
    """Session truth is deliberately independent from the presentation choice."""

    presentation: str = "a"
    selected_agent: str = "Research"
    command_open: bool = False
    message_count: int = len(MESSAGES)

    @rx.var
    def presentation_label(self) -> str:
        return "Atmosphere" if self.presentation == "a" else "Signal"

    @rx.var
    def morphology_class(self) -> str:
        return f"morph-{self.presentation}"

    def switch_presentation(self) -> None:
        self.presentation = "b" if self.presentation == "a" else "a"

    def choose_agent(self, agent: str) -> None:
        self.selected_agent = agent

    def toggle_command(self) -> None:
        self.command_open = not self.command_open

    def add_note(self) -> None:
        """A small stateful interaction to prove the session remains live."""
        self.message_count += 1
