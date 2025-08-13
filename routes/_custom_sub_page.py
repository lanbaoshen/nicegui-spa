from collections.abc import Callable

from nicegui import app, ui
from nicegui.page_arguments import RouteMatch

from pages import LoginPage


def protected(func: Callable) -> Callable:
    """Decorator to mark a route handler as requiring authentication for the custom_sub_pages."""
    func._is_protected = True  # pylint: disable=protected-access
    return func


class CustomSubPages(ui.sub_pages):
    def _render_page(self, match: RouteMatch) -> bool:
        if is_route_protected(match.builder) and not is_authenticated():
            self._login(match.full_url)
            return True
        return super()._render_page(match)

    def _login(self, intended_path: str) -> None:
        def callback():
            ui.run_javascript('window.location.reload();')
            ui.navigate.to(intended_path)

        LoginPage(callback=callback)


def is_route_protected(handler: Callable) -> bool:
    return getattr(handler, '_is_protected', False)


def is_authenticated() -> bool:
    return app.storage.user.get('authenticated', False)


def is_superuser() -> bool:
    return app.storage.user.get('is_superuser', False)


custom_sub_pages = CustomSubPages
