from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str = None


class ItemCreate(ItemBase):
    pass


class ItemEdit(ItemBase):
    id: str
    title: str = None
    description: str = None
