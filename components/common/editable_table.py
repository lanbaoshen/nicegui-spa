from typing import Any, Literal

from nicegui import events, ui


class EditableTable(ui.table):
    def __init__(self, *args, actions: list[Literal['add', 'edit', 'remove']] = None, **kwargs):
        if 'add' in actions:
            ui.button('Add', icon='add', on_click=self._add).classes('w-1/8 teal-btn')

        if not any(action in actions for action in ('edit', 'remove')):
            super().__init__(*args, **kwargs)
        else:
            kwargs.setdefault('columns', []).append({'name': 'action', 'label': 'Action', 'field': 'action'})
            super().__init__(*args, **kwargs)
            self._add_action(actions)

    def _add_action(self, actions: list[Literal['add', 'edit', 'remove']]):
        edit = (
            "<q-btn @click=\"$parent.$emit('edit', props)\" icon='edit' flat dense color='blue'/>"
            if 'edit' in actions
            else ''
        )
        remove = (
            "<q-btn @click=\"$parent.$emit('remove', props)\" icon='delete' flat dense color='red'/>"
            if 'remove' in actions
            else ''
        )

        self.add_slot(
            'body-cell-action',
            f"""
            <q-td :props="props">
                {edit}
                {remove}
            </q-td>
        """,
        )

        self.on('edit', lambda e: self._edit(self._get_row(e)))
        self.on('remove', lambda e: self._remove(self._get_row(e)))

    def _get_row(self, e: events.GenericEventArguments) -> dict[str, Any]:
        return e.args.get('row')

    def _add(self):
        ui.notify('Add row')

    def _edit(self, row: dict[str, Any]):
        ui.notify(row)

    def _remove(self, row: dict[str, Any]):
        ui.notify(row)
