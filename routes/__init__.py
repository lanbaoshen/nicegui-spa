from nicegui import ui

from components.common import ChatBox, HeaderNotification, Sidebar
from routes import admin, dashboard, item, user
from routes._custom_sub_page import custom_sub_pages, is_authenticated, is_superuser


@ui.page('/')
@ui.page('/{_:path}')
def main_page():
    HeaderNotification()

    items = [
        {'target': '/', 'label': 'Dashboard', 'icon': 'home'},
        {'target': '/item', 'label': 'Item', 'icon': 'book'},
        {'target': '/user/settings', 'label': 'User Settings', 'icon': 'settings'},
    ]
    sub_pages = {
        '/': dashboard.dashboard_page,
        '/item': item.item_page,
        '/user/settings': user.user_settings_page,
    }

    if is_superuser():
        items.append({'target': '/admin', 'label': 'Admin', 'icon': 'manage_accounts'})
        sub_pages.update(
            {
                '/admin': admin.admin_page,
            }
        )

    custom_sub_pages(sub_pages)

    if is_authenticated():
        Sidebar(items=items)

        ChatBox()
