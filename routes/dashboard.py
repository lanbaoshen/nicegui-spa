import theme
from pages.dashboard import DashboardPage
from routes._custom_sub_page import protected


@protected
def dashboard_page():
    with theme.frame('Dashboard'):
        DashboardPage()
