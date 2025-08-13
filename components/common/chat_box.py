from nicegui import ui


class ChatBox(ui.card):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.messages: list[tuple[str, str, str]] = []
        self.style('border: 2px solid teal;')
        self.classes('chat-box')
        self.visible = False

        self.content()

        self.messages.append(('Hi there! How can I help you today?', 'Assistant', '/static/favicon.png'))
        self.chat_messages.refresh()

    def content(self):
        with self:
            with ui.column().classes('w-full h-full') as self.message_container:
                self.chat_messages()

                with ui.row().classes('w-full gap-2 flex items-center'):
                    self.input = ui.input().props('fullwidth').classes('flex-grow')
                    self.send_btn = ui.button('Send', on_click=self.send).classes('teal-btn')

        ui.button(on_click=lambda: self.set_visibility(not self.visible), icon='android').props('flat').classes(
            'bot-btn'
        )

    @ui.refreshable
    def chat_messages(self) -> None:
        if self.messages:
            with ui.scroll_area().classes('w-full h-full max-h-full overflow-y-auto w-full') as scroll_area:
                for text, name, avatar in self.messages:
                    sent = name != 'Assistant'
                    ui.chat_message(text=text, name=name, avatar=avatar, sent=sent).classes('chat-message').classes(
                        'ml-auto' if sent else ''
                    )

            scroll_area.scroll_to(percent=100)

    def _bot(self, message: str):
        def response():
            self.messages.append((f'Hello! I am a bot. You said: {message}', 'Assistant', '/static/favicon.png'))
            self.chat_messages.refresh()

        ui.timer(1, response, once=True)

    def send(self):
        message = self.input.value.strip()
        if not message:
            return

        self.messages.append((message, 'User', '/static/favicon.png'))
        self._bot(message)
        self.input.value = ''
        self.chat_messages.refresh()
