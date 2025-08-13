from nicegui import ui

from . import chat_box, editor, notify, sidebar  # noqa: F401

ui.add_css(
    """
.teal-btn {
    background-color: teal !important;
}
.cancel-btn {
    background-color: #f8f9fa !important;
    color: black !important;
}
.navi-title {
    font-size: 1.5rem;
    margin-top: 0.75rem;
    font-weight: bold;
    transform: scaleX(1.1);
    transform-origin: left;
}
.rounded-btn {
    border-radius: 50%;
    padding: 0.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
}
.q-tab--active {
    color: teal !important;
}
.q-table, .q-table__container, .q-table__card {
    border: none !important;
    box-shadow: none !important;
}
.q-table .q-tr, .q-table .q-td {
    height: 50px !important;
}
.q-item__label {
    color: teal !important;
}
.nicegui-sub-pages {
    width: 100%
}
""",
    shared=True,
)
