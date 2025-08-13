from typing import Any
from uuid import uuid4

from nicegui import ui

from components.admin.user_editor import UserEditor
from components.common import EditableTable
from models.user import UserCreate, UserEdit


class UserTable(EditableTable):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('columns', []).extend(
            [
                {'name': 'username', 'field': 'username', 'label': 'Username'},
                {'name': 'name', 'field': 'name', 'label': 'Name'},
                {'name': 'email', 'field': 'email', 'label': 'Email'},
                {'name': 'is_superuser', 'field': 'is_superuser', 'label': 'Is Superuser'},
                {'name': 'is_active', 'field': 'is_active', 'label': 'Is Active'},
            ]
        )
        kwargs.setdefault('rows', [])
        kwargs.setdefault('pagination', {'rowsPerPage': 10})
        kwargs.setdefault('actions', ['add', 'edit'])

        super().__init__(*args, **kwargs)

    def _add(self):
        def callback(user: UserCreate):
            row = user.model_dump()
            row.update({'id': str(uuid4())})
            self.rows.append(row)
            self.update()
            ui.notify(f'Add user: {row}')

        UserEditor(value=True, callback=callback)

    def _edit(self, row: dict[str, Any]):
        def callback(user: UserEdit):
            new_row = user.model_dump()
            for row_ in self.rows:
                if row_['id'] == new_row['id']:
                    row_.update(new_row)

            self.update()
            ui.notify(f'Update user: {row} -> {new_row}')

        UserEditor(value=True, callback=callback, user=UserEdit(**row))
