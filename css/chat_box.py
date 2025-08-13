from nicegui import ui

ui.add_css(
    """
.bot-btn {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 1000;
    border-radius: 50%;
    padding: 0.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: teal !important;
    color: white !important;
}
.chat-box {
    position: fixed;
    right: 20px;
    bottom: 10vh;
    width: 25vw;
    height: 70vh;
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    padding: 16px;
    z-index: 1000;
}
.chat-message {
    font-size: 0.8rem;
}
""",
    shared=True,
)
