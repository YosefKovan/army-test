from sqlmodel import SQLModel, Field
from typing import Optional

class Soldiers(SQLModel, table=True):
    key :Optional[int] = Field(default=None, primary_key=True)
    military_id : str = Field(unique=True)
    first_name : str
    last_name : str
    sex : str
    city : str
    distance : int
    assigned : bool = Field(default=False)
    room : int = Field(foreign_key='rooms.key')




