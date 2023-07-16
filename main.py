import random

from fastapi import FastAPI,Response,status,HTTPException,Depends
from fastapi.params import Body
from otherdata.data import volume,status,trades,totalcompanies


app=FastAPI()

@app.get("/volume")
def volumefind():
    answer=volume()
    return {"Volume":answer}

@app.get("/status")
def statusfind():
    answer=status()
    return {"Market Status":answer}

@app.get("/trades")
def tradesfind():
    answer=trades()
    return {"Total Trades":answer}

@app.get("/totalcompanies")
def companiesfound():
    answer=totalcompanies()
    return {"Total Companies":answer}

