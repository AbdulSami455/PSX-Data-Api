import random

from fastapi import FastAPI,Response,status,HTTPException,Depends
from fastapi.params import Body
from otherdata.data import volume


app=FastAPI()

@app.get("/volume")
def volume():
    answer=volume()
    return {"Volume":answer}