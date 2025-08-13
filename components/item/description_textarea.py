from nicegui import ui


class DescriptionTextarea(ui.textarea):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('validation', self.valid_func)
        kwargs.setdefault('label', 'Description')
        super().__init__(*args, **kwargs)
        self._auto_validation = False

    @staticmethod
    def valid_func(value: str) -> None | str:
        return None if len(value) < 2048 else 'The length must be less than 2048.'
