from sqlmodel import SQLModel, create_engine, Session
from app.models.rooms import Rooms
from app.models.dorms import Dorms
from app.models.soldiers import Soldiers


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session