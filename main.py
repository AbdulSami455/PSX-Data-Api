import random

from fastapi import FastAPI,Response,status,HTTPException,Depends
from fastapi.params import Body
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from otherdata.data import volume,status,trades,totalcompanies,companiesinprofit,companiesinloss
from pydantic import BaseModel
from datetime import datetime,timedelta
from jose import JWTError,jwt
from passlib.context import CryptContext


SECRET_KEY="e12e7c906399ccd916412da0ce9013698159e819a8dbe989cc31251823d9fe5c"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

class data(BaseModel):
    name:str

fake_db={"sami":{
    "username":"sami",
    "full_name":"Abdul Sami",
    "email":"sami@gmail.com",
    "hashed_password":"",
    "disabled":False

}}

class Token(BaseModel):
   access_type:str
   token_type:str

class Tokendata(BaseModel):
    username:str or None=None

class User(BaseModel):
    username:str
    email:str or None = None
    full_name:str or None=None

class userindb(User):
    hashed_password:str

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

app=FastAPI()

def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db,username:str):
    if username in db:
        user_data=db[username]
        return userindb(""user_data)







@app.post("/index")
def fgfg(name:data):
    return {"hello":name}

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

@app.get("/companiesinprofit")
def companiesinprofitfound():
    answer=companiesinprofit()
    return {"Number of Companies in Profit":answer}