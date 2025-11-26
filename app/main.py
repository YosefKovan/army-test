from fastapi import FastAPI
from fastapi import FastAPI, UploadFile, File

from app.services.placement_service import place_soldiers
from services.csv_reader import csv_to_dict
from services.soldiers_service import create_soldiers
from app.memory_data import data
from services.json_service import get_json_format


app = FastAPI()


@app.post("/upload/soldiers/csv")
async def assign_with_csv(file : UploadFile = File(...)):
    """this path will read and write the data from the csv file"""

    csv_dict = await csv_to_dict(file)
    data.soldiers = create_soldiers(csv_dict)
    place_soldiers(dorms=data.dorms, soldiers=data.soldiers, waiting_list=data.waiting_list)
    return get_json_format(data.soldiers, data.dorms, data.waiting_list)





