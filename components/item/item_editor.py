from collections.abc import Callable

from nicegui import ui

from components.item.description_textarea import DescriptionTextarea
from components.item.title_input import TitleInput
from models.item import ItemCreate, ItemEdit


class ItemEditor(ui.dialog):
    def __init__(self, *args, callback: Callable, item: ItemEdit = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._callback = callback

        with self:
            with ui.card().classes('w-[60vw]'):
                ui.label('Add Item').classes('editor-title')

                self.title = TitleInput(value=item.title if item else '').classes('editor-input')
                self.description = DescriptionTextarea(value=item.description if item else '').classes(
                    'editor-textarea'
                )

                with ui.row().classes('w-full justify-end gap-2'):
                    ui.button('Edit' if item else 'ADD', on_click=lambda: self.save(item)).classes('teal-btn')
                    ui.button('Cancel', on_click=self.close).classes('cancel-btn')

    def save(self, item: ItemEdit = None):
        if not all([input_.validate() for input_ in (self.title, self.description)]):  # noqa: C419
            return

        if item:
            item.title = self.title.value
            item.description = self.description.value
            self._callback(item)
        else:
            self._callback(
                ItemCreate(
                    title=self.title.value,
                    description=self.description.value,
                )
            )

        self.close()
