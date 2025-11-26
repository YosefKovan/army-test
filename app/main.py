from fastapi import FastAPI
from fastapi import FastAPI, UploadFile, File
from services.csv_reader import csv_to_dict
from services.soldiers_service import create_soldiers



app = FastAPI()


@app.post("/upload/soldiers/csv")
async def login_func(file : UploadFile = File(...)):
    """this path will read and write the data from the csv file"""
    csv_dict = await csv_to_dict(file)
    return create_soldiers(csv_dict)

