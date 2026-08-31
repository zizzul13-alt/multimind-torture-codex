import reflex as rx

from .components import agent_constellation, command_sheet, conversation, decision_strip, mobile_dock, wordmark
from .state import BenchmarkState


def topbar() -> rx.Component:
    return rx.el.header(
        wordmark(),
        rx.el.div(
            rx.el.span("PRESENTATION", class_name="top-label"),
            rx.el.button(
                rx.el.span(BenchmarkState.presentation_label, class_name="presentation-name"),
                rx.el.span("↗", class_name="presentation-arrow"),
                on_click=BenchmarkState.switch_presentation,
                class_name="presentation-switch",
                data_morph_switch="true",
                aria_label="Switch presentation without reloading the session",
            ),
            class_name="presentation-control",
        ),
        class_name="topbar",
    )


def index() -> rx.Component:
    return rx.el.main(
        rx.el.div(class_name="material-noise", aria_hidden=True),
        rx.el.div(class_name="material-orb orb-one", aria_hidden=True),
        rx.el.div(class_name="material-orb orb-two", aria_hidden=True),
        topbar(),
        rx.el.div(agent_constellation(), conversation(), decision_strip(), class_name="workspace"),
        mobile_dock(),
        command_sheet(),
        class_name=BenchmarkState.morphology_class,
        id="multimind-app",
    )


app = rx.App(
    stylesheets=["/benchmark.css"],
    head_components=[
        rx.el.meta(name="viewport", content="width=device-width, initial-scale=1"),
        rx.script(src="/scroll-preservation.js"),
    ],
)
app.add_page(index, route="/", title="MultiMind / Reflex torture benchmark")
