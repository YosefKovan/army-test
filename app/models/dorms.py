from sqlmodel import SQLModel, Field
from typing import Optional

class Dorms(SQLModel, table=True):
    key : Optional[int] = Field(default=None, primary_key=True)
    dorm_number : int





