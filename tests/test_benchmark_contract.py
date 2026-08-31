"""Focused contract tests for the isolated Reflex benchmark.

These inspect source-level guarantees that do not need a running browser. Browser
steps are documented in evidence/VALIDATION.md for environments with Reflex.
"""
from pathlib import Path


ROOT = Path(__file__).parents[1]


def source(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def test_reflex_app_has_a_single_root_surface_and_local_ports():
    app = source("multimind_reflex/multimind_reflex.py")
    config = source("rxconfig.py")
    assert "rx.App(" in app
    assert 'route="/"' in app
    assert "frontend_port=3092" in config
    assert "backend_port=8092" in config


def test_live_morphology_is_state_driven_not_navigation_driven():
    state = source("multimind_reflex/state.py")
    app = source("multimind_reflex/multimind_reflex.py")
    assert 'presentation: str = "a"' in state
    assert 'self.presentation = "b" if self.presentation == "a" else "a"' in state
    assert "BenchmarkState.switch_presentation" in app
    assert "redirect" not in state.lower()
    assert "window.location" not in app.lower()


def test_session_truth_is_separate_from_presentation_truth():
    state = source("multimind_reflex/state.py")
    data = source("multimind_reflex/data.py")
    assert "message_count" in state
    assert "MESSAGES" in data
    assert "selected_agent" in state
    assert "switch_presentation" in state


def test_mobile_is_a_dedicated_navigation_and_thread_composition():
    css = source("assets/benchmark.css")
    components = source("multimind_reflex/components.py")
    assert ".mobile-dock" in css
    assert "@media (max-width: 760px)" in css
    assert "Mobile session navigation" in components
    assert ".agent-constellation, .decision-strip { display: none" in css


def test_scroll_preservation_uses_owned_data_attribute_not_framework_dom_hacks():
    js = source("assets/scroll-preservation.js")
    assert "data-scroll-region='conversation'" in js
    assert "data-morph-switch" in js
    assert "sessionStorage" in js
    assert "MutationObserver" in js
    assert "reflex" not in js.lower()


def test_material_motion_and_reduced_motion_are_present():
    css = source("assets/benchmark.css")
    assert 'url("/grain.svg")' in css
    assert "material-orb" in css
    assert "@keyframes pulse" in css
    assert "prefers-reduced-motion" in css
