from collections.abc import Callable

from nicegui import app, ui

from components.user import PasswordInput, UsernameInput


class LoginPage:
    def __init__(self, callback: Callable):
        self._callback = callback
        with ui.element('div').classes('fixed inset-0 flex items-center justify-center'):
            with ui.element().classes('p-4 w-1/3 max-w-lg'):
                with ui.column().classes('items-center gap-4 w-full'):
                    ui.image('/static/fastapi-logo.svg').classes('w-3/5')
                    self.username = UsernameInput().classes('w-4/5')
                    self.password = PasswordInput().classes('w-4/5')
                    ui.link('Forgot password?', '#').classes('text-s text-blue-500 no-underline')
                    ui.button('LOG IN', on_click=self.login).classes('bg-blue-500 w-4/5 teal-btn')

    def login(self):
        if all([input_.validate() for input_ in (self.username, self.password)]):  # noqa: C419
            try:
                if self.username.value == 'lanbao':
                    app.storage.user['authenticated'] = True
                    app.storage.user['is_superuser'] = True
                    ui.notify('Login successful', type='positive')
                elif self.username.value == 'normal':
                    app.storage.user['authenticated'] = True
                    app.storage.user['is_superuser'] = False
                    ui.notify('Login successful', type='positive')
                else:
                    raise ValueError('Invalid username or password')  # noqa: EM101

                self._callback()

            except Exception as e:
                ui.notify(e, type='negative')
