from fastapi import FastAPI, UploadFile
import csv


async def csv_to_dict(file : UploadFile):
    """this will return the csv as a python dict"""
    raw = await file.read()
    text = raw.decode("utf-8")
    lines = text.split("\n")
    return csv.DictReader(lines)