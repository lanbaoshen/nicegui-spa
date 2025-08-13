from collections.abc import Callable

from nicegui import ui


class Confirm(ui.dialog):
    def __init__(self, *args, message: str, callback: Callable = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = message
        self.callback = callback

        with self:
            with ui.card().classes('w-96'):  # fixed width card
                ui.label('Confirm').classes('text-xl font-bold')

                ui.label(self.message).classes('text-center w-full')

                with ui.row().classes('w-full justify-between gap-4 px-10'):
                    ui.button('Confirm', on_click=self._confirm).classes('teal-btn')
                    ui.button('Cancel', on_click=self.close).classes('cancel-btn')

    def _confirm(self):
        self.callback()
        self.close()
