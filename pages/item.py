from uuid import uuid4

from components.item import ItemTable


class ItemPage:
    def __init__(self):
        self.table = ItemTable(
            rows=[
                {
                    'id': str(uuid4()),
                    'title': 'Item 1',
                    'description': 'Description for Item 1',
                },
                {
                    'id': '2',
                    'title': 'Item 2',
                },
            ]
        ).classes('w-full')
