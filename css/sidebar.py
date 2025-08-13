from nicegui import ui

ui.add_css(
    """
.left-drawer {
    background-color: #f8f9fa !important;
}
.left-drawer-toggle {
    position: fixed;
    bottom: 20px;
    left: 20px;
    z-index: 1000;
    background-color: #f8f9fa !important;
    color: teal !important;
}
.image-container {
    display: flex;
    justify-content: center;
    width: 100%;
    padding: 1rem 0;
}
.sidebar-row {
    display: flex;
    align-items: center;
    gap: 0.25rem;
    padding: 0.25rem 0.5rem;
    cursor: pointer;
    transition: background 0.2s;
}
.sidebar-row:hover {
    color: teal;
}
.sidebar-icon {
    color: teal;
    font-size: 1.5rem;
}
.sidebar-label {
    color: teal;
    font-size: 1.25rem;
}
""",
    shared=True,
)
