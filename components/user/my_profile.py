from nicegui import ui

from components.user.email_input import EmailInput
from components.user.name_input import NameInput


class MyProfile:
    def __init__(self):
        ui.label('User Information').classes('text-bold text-xl')
        name = NameInput(value='Lanbao').classes('w-1/2')
        email = EmailInput(value='lanbao@example.com').classes('w-1/2')

        ui.button(
            'Save', on_click=lambda: ui.notify(f'Save name: {name.value}, {email.value}', type='positive')
        ).classes('teal-btn')
