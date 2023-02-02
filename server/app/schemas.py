from typing import Union

from pydantic import BaseModel


class RecordBase(BaseModel):
    title: str
    description: Union[str, None] = None


class RecordCreate(RecordBase):
    pass


class Record(RecordBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    records: list[Record] = []

    class Config:
        orm_mode = True