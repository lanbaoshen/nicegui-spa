from random import choice

from nicegui import ui


class HeaderNotification(ui.header):
    def __init__(self, *args, **kwargs):
        if notifs := self._get_notify():
            super().__init__(*args, **kwargs)
            self.notifs = notifs

            with self.classes('notify'):
                with ui.row().classes('items-center w-full flex'):
                    ui.icon('notifications_active').classes('notify-icon')
                    self.notif_label = ui.label().classes('notify-label')
                    ui.button(icon='close', on_click=lambda: self.set_visibility(False)).classes('text-white').props(
                        'flat dense'
                    )

            ui.timer(5.0, self.update_notif)

    def _get_notify(self) -> list[str]:
        return ['TODO', 'Lanbao', 'Hello World']

    def update_notif(self):
        notification = choice(self.notifs)  # noqa: S311
        self.notif_label.set_text(notification)
