import random

from fastapi import FastAPI,Response,status,HTTPException,Depends
from fastapi.params import Body
from otherdata.data import volume


app=FastAPI()

@app.get("/volume")
def volumefind():
    answer=volume()
    return {"Volume":answer}

