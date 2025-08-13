from nicegui import ui

from components.user import MyProfile


class UserSettingsPage:
    def __init__(self):
        with ui.tabs() as tabs:
            ui.tab('My Profile')
            ui.tab('Password')

        with ui.tab_panels(tabs, value='My Profile').classes('w-full'):
            with ui.tab_panel('My Profile'):
                MyProfile()
