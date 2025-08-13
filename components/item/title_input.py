from nicegui import ui


class TitleInput(ui.input):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('validation', self.valid_func)
        kwargs.setdefault('label', 'Title')
        super().__init__(*args, **kwargs)
        self._auto_validation = False

    @staticmethod
    def valid_func(value: str) -> None | str:
        return None if 1 < len(value) < 120 else 'The length must be greater than 1 and less than 120.'
