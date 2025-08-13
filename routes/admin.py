import theme
from pages import AdminPage
from routes._custom_sub_page import protected


@protected
def admin_page():
    with theme.frame('User Management'):
        AdminPage()
