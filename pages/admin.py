import uuid

from components.admin import UserTable


class AdminPage:
    def __init__(self):
        self.table = UserTable(
            rows=[
                {
                    'id': str(uuid.uuid4()),
                    'username': 'lanbao',
                    'name': 'Lanbao',
                    'email': 'test@example.com',
                    'is_superuser': True,
                    'is_active': True,
                },
                {
                    'id': str(uuid.uuid4()),
                    'username': 'normal',
                    'name': 'normal',
                    'email': 'test@example.com',
                    'is_superuser': False,
                    'is_active': True,
                },
            ]
        ).classes('w-full')
