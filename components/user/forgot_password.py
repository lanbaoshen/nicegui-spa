from nicegui import ui

from components.user import EmailInput, UsernameInput


class ForgotPassword(ui.dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        with self:
            with ui.card().classes('w-96'):  # fixed width card
                ui.label('Forgot Password').classes('text-xl font-bold')

                self.username = UsernameInput().classes('editor-input')
                self.email = EmailInput().classes('editor-input')

                with ui.row().classes('w-full justify-end gap-2'):
                    ui.button('Send', on_click=self.send).classes('teal-btn')
                    ui.button('Cancel', on_click=self.close).classes('cancel-btn')

    def send(self):
        if not all([input_.validate() for input_ in (self.username, self.email)]):  # noqa: C419
            return

        if self.username.value not in ['lanbao', 'normal']:
            ui.notify('Invalid username', type='negative')
        elif self.email.value != 'test@example.com':
            ui.notify('Invalid email', type='negative')
        else:
            ui.notify('Password reset link sent to your email', type='positive')
            self.close()
