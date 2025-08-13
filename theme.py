from contextlib import contextmanager

from nicegui import app, ui


@contextmanager
def frame(title: str):
    def logout():
        app.storage.user['authenticated'] = False
        ui.run_javascript('window.location.reload();')

    with ui.row().classes('w-full gap-2 flex items-center'):
        ui.label(title).classes('navi-title')
        with ui.button(icon='account_circle', color='teal').classes('rounded-btn ml-auto'):
            with ui.menu():
                ui.button('Logout', on_click=logout).classes('teal-btn')

    yield
