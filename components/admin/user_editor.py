from collections.abc import Callable

from nicegui import ui

from components.user import EmailInput, NameInput, PasswordInput, UsernameInput
from models.user import UserCreate, UserEdit


class UserEditor(ui.dialog):
    def __init__(self, *args, callback: Callable, user: UserEdit = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._callback = callback

        with self:
            with ui.card().classes('w-96'):  # fixed width card
                ui.label('Add User').classes('text-xl font-bold')

                self.username = (
                    UsernameInput(value=user.username if user else '')
                    .classes('editor-input')
                    .props('readonly' if user else '')
                )
                self.name = NameInput(value=user.name if user else '').classes('editor-input')
                self.email = EmailInput(value=user.email if user else '').classes('editor-input')
                if not user:
                    self.password = PasswordInput().classes('editor-input')

                with ui.row().classes('w-full'):
                    self.is_superuser = ui.checkbox('Is Superuser?', value=user.is_superuser if user else False)
                    self.is_active = ui.checkbox('Is Active?', value=user.is_active if user else True)

                with ui.row().classes('w-full justify-end gap-2'):
                    ui.button('Add', on_click=lambda: self.save(user)).classes('teal-btn')
                    ui.button('Cancel', on_click=self.close).classes('cancel-btn')

    def save(self, user: UserEdit = None):
        check_list = [self.username, self.name, self.email]
        if not user:
            check_list.append(self.password)
        if not all([input_.validate() for input_ in check_list]):  # noqa: C419
            return

        if user:
            user.name = self.name.value
            user.email = self.email.value
            user.is_active = self.is_active.value
            user.is_superuser = self.is_superuser.value
            self._callback(user)
        else:
            self._callback(
                UserCreate(
                    username=self.username.value,
                    name=self.name.value,
                    email=self.email.value,
                    password=self.password.value,
                    is_active=self.is_active.value,
                    is_superuser=self.is_superuser.value,
                )
            )

        self.close()
