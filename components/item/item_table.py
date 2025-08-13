from typing import Any
from uuid import uuid4

from nicegui import ui

from components.common import Confirm, EditableTable
from components.item.item_editor import ItemEditor
from models.item import ItemCreate, ItemEdit


class ItemTable(EditableTable):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('columns', []).extend(
            [
                {'name': 'title', 'field': 'title', 'label': 'Title'},
                {'name': 'description', 'field': 'description', 'label': 'Description'},
            ]
        )
        kwargs.setdefault('rows', [])
        kwargs.setdefault('pagination', {'rowsPerPage': 10})
        kwargs.setdefault('actions', ['add', 'edit', 'remove'])

        super().__init__(*args, **kwargs)

    def _remove(self, row: dict[str, Any]):
        def callback():
            self.rows[:] = [row_ for row_ in self.rows if row_['id'] != row['id']]
            ui.notify(f'Remove row with ID {row["id"]}')
            self.update()

        Confirm(value=True, message=f'Remove item: {row["title"]}?', callback=callback)

    def _add(self):
        def callback(item: ItemCreate):
            row = item.model_dump()
            row.update({'id': str(uuid4())})
            self.rows.append(row)
            self.update()
            ui.notify(f'Add item: {row}')

        ItemEditor(value=True, callback=callback)

    def _edit(self, row: dict[str, Any]):
        def callback(item: ItemEdit):
            new_row = item.model_dump()
            for row_ in self.rows:
                if row_['id'] == new_row['id']:
                    row_.update(new_row)

            self.update()
            ui.notify(f'Update item: {row} -> {new_row}')

        ItemEditor(value=True, callback=callback, item=ItemEdit(**row))
