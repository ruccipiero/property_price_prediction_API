import json
import pandas as pd
from fastapi import FastAPI, status #, File, UploadFile
import predict.prediction as pp
import preprocessing.cleaning_data as pc
from pydantic import BaseModel
from typing import Union
import uvicorn

#raise HTTPException
app = FastAPI()

class Data(BaseModel):
    area: int
    property_type: str
    rooms_number: int
    zip_code: int 
    land_area: int
    garden: bool
    garden_area: int
    equipped_kitchen: bool
    full_address: str | None
    swimming_pool: bool
    furnished: bool
    open_fire: bool 
    terrace: bool
    terrace_area: int
    facades_number: int
    building_state: str

class Item1(BaseModel):
    data: Data


# / -> Just return Alive! if the API is running
@app.get("/")
async def alive():
    return "Alive!"

# GET /predict return a string with the schema of the input expected. That's just for documentation purpose. (Yes FastAPI is already generating a nice documentation, it's just for the exercice)
@app.get("/predict")
async def scheme():
    data_string="""    area: int
    property_type: str
    rooms_number: int
    zip_code: int 
    land_area: int
    garden: bool
    garden_area: int
    equipped_kitchen: bool
    full_address: str | None
    swimming_pool: bool
    furnished: bool
    open_fire: bool 
    terrace: bool
    terrace_area: int
    facades_number: int
    building_state: str"""
    return data_string

@app.post("/predict")
async def predict(item: Item1):
    """That takes the property details as input and return the prediction as output"""
    clean_dict = pc.preprocess(item)
    price = pp.predict(clean_dict)
    return {"prediction:": price}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
