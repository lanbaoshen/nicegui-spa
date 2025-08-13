from nicegui import ui

ui.add_css(
    """
.notify {
    background-color: teal !important;
}

.notify-icon {
    font-size: 1.25rem;
    margin-left: 2rem;
}

.notify-label {
    font-size: 1rem;
}
""",
    shared=True,
)
