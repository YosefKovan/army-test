from fastapi import FastAPI, HTTPException
from fastapi import FastAPI, UploadFile, File, Depends
from app.memory_data import data
from services.router_service import *
from app.database.db import *

app = FastAPI()

#this will create the schemes and the database
create_db_and_tables()

@app.post("/upload/soldiers/csv")
async def assign_with_csv(file : UploadFile = File(...), session: Session = Depends(get_session)):
    """this path will read and write the data from the csv file"""
    return await assign_with_csv_service(session, file, data.soldiers, data.dorms, data.waiting_list)


@app.get("/space")
def space():
    return data.dorms.get_space()


@app.get("/waitingList")
def waiting_list():
    return {"waiting list" : data.waiting_list.get_soldiers()}


@app.get("/search/{military_id}")
def search_by_military_id(military_id : str):
    return search_by_military_id_service(military_id, data.soldiers)









