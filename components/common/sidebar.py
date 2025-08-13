from nicegui import ui


class SidebarItem(ui.row):
    def __init__(self, *args, icon: str, label: str, **kwargs):
        super().__init__(*args, **kwargs)
        with self.classes('sidebar-row'):
            ui.icon(icon).classes('sidebar-icon')
            ui.label(label).classes('sidebar-label')


class Sidebar(ui.left_drawer):
    def __init__(self, *args, items: list[dict[str, str]], **kwargs):
        super().__init__(*args, **kwargs)

        with self.classes('left-drawer'):
            with ui.element('div').classes('image-container'):
                ui.image(source='/static/fastapi-logo.svg').props('width=70%')
            for item in items:
                SidebarItem(icon=item.get('icon', ''), label=item.get('label', '')).on(
                    'click', lambda target=item.get('target', '#'): ui.navigate.to(target)
                )

        ui.button(on_click=lambda: self.toggle(), icon='menu').props('flat').classes('left-drawer-toggle')
