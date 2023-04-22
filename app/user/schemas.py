from typing import List
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: str

    class Config:
        orm_mode = True

class UserList(BaseModel):
    total: int
    items: List[UserOut]
