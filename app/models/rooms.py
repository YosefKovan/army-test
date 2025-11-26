
from sqlmodel import SQLModel, Field
from typing import Optional

class Rooms(SQLModel, table=True):
    key :Optional[int] = Field(default=None, primary_key=True)
    room_number : int
    dorm_number : int = Field(foreign_key='dorms.dorm_number')
    max_capacity : int

