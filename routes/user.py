import theme
from pages import UserSettingsPage
from routes._custom_sub_page import protected


@protected
def user_settings_page():
    with theme.frame('User Settings'):
        UserSettingsPage()
