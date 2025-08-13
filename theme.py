from contextlib import contextmanager

from nicegui import ui


@contextmanager
def frame(title: str):
    ui.label(title).classes('navi-title')

    yield
