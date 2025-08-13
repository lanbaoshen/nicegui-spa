from pathlib import Path
from uuid import uuid4

from nicegui import app, ui

import css  # noqa: F401

app.add_static_files('/static', Path(__file__).parent / 'static')

# https://github.com/zauberzeug/nicegui/pull/4821
# https://github.com/zauberzeug/nicegui/pull/5005
import routes  # noqa: F401, E402

# TODO
ui.run(storage_secret=str(uuid4()))
