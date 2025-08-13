from nicegui import ui

from components.user.email_input import EmailInput
from components.user.name_input import NameInput


class MyProfile:
    def __init__(self):
        ui.label('User Information').classes('text-bold text-xl')
        self.name = NameInput(value='Lanbao').classes('w-1/2')
        self.email = EmailInput(value='lanbao@example.com').classes('w-1/2')

        ui.button('Save', on_click=self.save).classes('teal-btn')

    def save(self):
        if not all([input_.validate() for input_ in (self.name, self.email)]):  # noqa: C419
            return

        ui.notify(f'Save name: {self.name.value}, {self.email.value}', type='positive')
