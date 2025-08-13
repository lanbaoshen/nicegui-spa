from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    name: str
    email: EmailStr

    is_active: bool = True
    is_superuser: bool = False


class UserCreate(UserBase):
    password: str


class UserEdit(UserBase):
    id: str
    name: str = None
    email: EmailStr = None
