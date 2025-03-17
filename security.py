import datetime
import os
from typing import Optional
from dotenv import load_dotenv

from fastapi import HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
import jose.jwt
from database.config import user_table, database

from passlib.context import CryptContext

load_dotenv()

pwd_content =CryptContext(schemes=["bcrypt"])
SECRET_KEY = os.getenv("SECRET_KEY") 

if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set!")
ALGORITHM="HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_password_hash(password:str):
    return pwd_content.hash(password)

def verify_password(password: str, hashed_password: str):
    return pwd_content.verify(password, hashed_password)

def create_token(id:int):
    expire = datetime.datetime.now(datetime.timezone.utc)+datetime.timedelta(minutes=30)
    expire = int(expire.timestamp()) 
    jwt_data = {"sub":str(id), "exp":expire}
    encoded_jwt = jose.jwt.encode(jwt_data,key=SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_user(email: str) -> Optional[dict]:
    query = user_table.select().where(user_table.c.email==email)
    result = await database.fetch_one(query)
    return result

def decode_token(token: str):
    try:
        payload = jose.jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jose.jwt.JWTError:
        raise HTTPException(status_code=401,detail="Invalid token")
    
async def get_current_user(token: str=Security(oauth2_scheme)):
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    return payload
def get_current_user_id(token: str=Security(oauth2_scheme)):
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    user_id = int(payload.get("sub"))
    return user_id
# async def get_pwd(password: str):
    # cond2=user_table.select().where(user_table.c.password==password)
    # result = await database.fetch_one(cond2)
    # if result:
        # return result