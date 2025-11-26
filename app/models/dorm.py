import sqlmodel
from sqlmodel import SQLModel, Field


class Dorm(SQLModel, table=True):
    id : int = Field()
