import random
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import  CryptContext
from datetime import datetime, timedelta
from pydantic import BaseModel
from otherdata.data import volume,status,companiesinloss,companiesinprofit,totalcompanies,trades
from sectorwise.sectors import somesector,numberofshare,indicesshare,sectorsshare
from indices.getcompanydata import companydata,getcompanyprofile,equityprofile
from indices.idetail import getindices,listofindices,listofcompanieswithprofit
SECRET_KEY = "27437940fd78c03104d9ab1d38095d187a96cf8aeeb1f5d74dde00afe6aa423f"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120

class User(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

fake_users_db = {}

new_username = "abdulsami"
new_password = "1234"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

fake_users_db[new_username] = {
    "username": new_username,
    "hashed_password": get_password_hash(new_password),
}

def authenticate_user(username: str, password: str):
    if username in fake_users_db:
        user = fake_users_db[username]
        if verify_password(password, user["hashed_password"]):
            return user

    return None

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

app = FastAPI()

@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/protected")
async def protected_route(token: str = Depends(OAuth2PasswordBearer(tokenUrl="/token"))):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

    return {"message": "You are authenticated!"}



@app.get("/volume")
async def find_volume(token: str = Depends(OAuth2PasswordBearer(tokenUrl="/token"))):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")

        # Perform the volume calculation or any other protected operatio
        answer = volume()

        return {"Total Volume of Stock Market": answer}

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")


@app.get("/status")
def findstatus(token: str = Depends(OAuth2PasswordBearer(tokenUrl="/token"))):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")

        # Perform the volume calculation or any other protected operatio
        answer = status()

        return {"Status of Stock Market is ": answer}

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

@app.get("/tradesinstockmarket")
def totaltrades(token: str = Depends(OAuth2PasswordBearer(tokenUrl="/token"))):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")

        # Perform the volume calculation or any other protected operatio
        answer = trades()

        return {"total trades done in stock market are ": answer}

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")


@app.get("/totalcompanies")
def totalcompanies(token: str = Depends(OAuth2PasswordBearer(tokenUrl="/token"))):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")

        # Perform the volume calculation or any other protected operatio
        answer = totalcompanies()

        return {"total trades done in stock market are ": answer}

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

@app.get("/companiesinloss")
def companiesinlossfind(token: str = Depends(OAuth2PasswordBearer(tokenUrl="/token"))):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")

        # Perform the volume calculation or any other protected operatio
        answer = companiesinloss()

        return {"Number of Companies in Loss ": answer}

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")


@app.get("/companiesinprofit")
def companiesinprofit(token: str = Depends(OAuth2PasswordBearer(tokenUrl="/token"))):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")

        # Perform the volume calculation or any other protected operatio
        answer = companiesinprofit()

        return {"Number of Companies in Profit ": answer}

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

@app.get("/sectors")
def allsectors(token: str = Depends(OAuth2PasswordBearer(tokenUrl="/token"))):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")

        # Perform the volume calculation or any other protected operatio
        answer = somesector()

        return {"All Listed Sectors ": answer}

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

@app.get("/sectorgraph")
def sectorgraph(token: str = Depends(OAuth2PasswordBearer(tokenUrl="/token"))):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")

        # Perform the volume calculation or any other protected operatio
        answer = sectorsshare()

        return {"All Listed Sectors ": answer}

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

@app.post("/{company}/getalldata")
def getcompanyalldata(company:str,token: str = Depends(OAuth2PasswordBearer(tokenUrl="/token"))):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")

        # Perform the volume calculation or any other protected operatio
        answer = companydata(company)

        return {"companydata": answer}

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

@app.post("/{company}/descprition")
def descrpitionofcompany(company:str,token: str = Depends(OAuth2PasswordBearer(tokenUrl="/token"))):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")

        # Perform the volume calculation or any other protected operatio
        answer = getcompanyprofile(company)

        return {"Company Details": answer}

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

@app.post("/{company}/equitydata")
def equitydatacompany(company:str,token: str = Depends(OAuth2PasswordBearer(tokenUrl="/token"))):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")

        # Perform the volume calculation or any other protected operatio
        answer = equityprofile(company)

        return {"Company Details": answer}

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
@app.get("/allindices")
def alllistindices(token: str = Depends(OAuth2PasswordBearer(tokenUrl="/token"))):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")

        # Perform the volume calculation or any other protected operatio
        answer = listofindices()

        return {"All Indices": answer}

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")


#get Value of ANy index
@app.get("/getindex")
def getindexvalue(indexname:str,token: str = Depends(OAuth2PasswordBearer(tokenUrl="/token"))):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")

        # Perform the volume calculation or any other protected operatio
        answer = getindices(indexname)

        return {"Index Value Now": answer}

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")