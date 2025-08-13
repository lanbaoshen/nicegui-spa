import theme
from pages import ItemPage
from routes._custom_sub_page import protected


@protected
def item_page():
    with theme.frame('Item Management'):
        ItemPage()
