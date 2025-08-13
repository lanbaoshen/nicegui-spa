from nicegui import ui

from components.user import PasswordInput


class UpdatePassword:
    def __init__(self):
        ui.label('Update Password').classes('text-bold text-xl')
        self.origin_password = PasswordInput(label='Origin Password').classes('w-1/2')
        self.new_password = PasswordInput(label='New Password').classes('w-1/2')
        self.confirm_password = PasswordInput(label='Confirm New Password').classes('w-1/2')

        ui.button('Save', on_click=self.save).classes('teal-btn')

    def save(self):
        if not all([input_.validate() for input_ in (self.origin_password, self.new_password, self.confirm_password)]):  # noqa: C419
            return

        if self.new_password.value != self.confirm_password.value:
            ui.notify('New password and confirm password do not match', type='negative')
            return

        ui.notify('Save new password', type='positive')
