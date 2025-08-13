from nicegui import ui

ui.add_css(
    """
.editor-title {
    font-size: 1.25rem;
    line-height: 1.75rem;
    font-weight: 700;
}
.editor-input {
    width: 100%;
}
.editor-textarea {
    width: 100%;
}
""",
    shared=True,
)
