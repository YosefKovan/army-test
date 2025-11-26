from fastapi import FastAPI, HTTPException
from fastapi import FastAPI, UploadFile, File
from app.services.placement_service import place_soldiers
from services.csv_reader import csv_to_dict
from services.soldiers_service import create_soldiers
from app.memory_data import data
from services.json_service import get_json_format
from services.router_service import *


app = FastAPI()


@app.post("/upload/soldiers/csv")
async def assign_with_csv(file : UploadFile = File(...)):
    """this path will read and write the data from the csv file"""
    return await assign_with_csv_service(file, data.soldiers, data.dorms, data.waiting_list)


@app.get("/space")
def space():
    return data.dorms.get_space()


@app.get("/waitingList")
def waiting_list():
    return {"waiting list" : data.waiting_list.get_soldiers()}


@app.get("/search/{military_id}")
def search_by_military_id(military_id : str):
    return search_by_military_id_service(military_id, data.soldiers)









