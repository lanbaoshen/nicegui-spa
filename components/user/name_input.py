from nicegui import ui


class NameInput(ui.input):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('validation', self.valid_func)
        kwargs.setdefault('label', 'Name')

        super().__init__(*args, **kwargs)
        self._auto_validation = False

    @staticmethod
    def valid_func(value: str) -> None | str:
        return 'The length must be greater than 5.' if not len(value) > 5 else None
