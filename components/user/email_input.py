from nicegui import ui
from pydantic import validate_email


class EmailInput(ui.input):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('validation', self.valid_func)
        kwargs.setdefault('label', 'Email')

        super().__init__(*args, **kwargs)
        self._auto_validation = False

    @staticmethod
    def valid_func(value: str) -> None | str:
        try:
            validate_email(value)
            return None
        except ValueError:
            return 'Invalid email format'
