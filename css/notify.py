from nicegui import ui

ui.add_css(
    """
.notify {
    background-color: teal !important;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem;
}
.notify-icon {
    font-size: 1.25rem;
    margin-left: 2rem;
}
.notify-label {
    font-size: 1rem;
    flex-grow: 1;
    text-align: left;
    margin-left: 1rem;
}
""",
    shared=True,
)
