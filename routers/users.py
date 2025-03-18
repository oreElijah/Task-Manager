from fastapi import APIRouter, HTTPException, status
from database.config import user_table, database

from models.users import UserIn, UserLogin
from security import create_token, get_password_hash, get_user, verify_password

router = APIRouter()

@router.get("/users", status_code=200)
async def get_users():
    query = user_table.select()
    return await database.fetch_all(query)

@router.post("/register", status_code=201)
async def register_user(user: UserIn):
    cond = await get_user(user.email)
    if cond:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with the email already exists")
    hashed_password = get_password_hash(user.password)
    query = user_table.insert().values(first_name=user.first_name, middle_name=user.middle_name, last_name=user.last_name, email=user.email, password = hashed_password)
    user_id = await database.execute(query)
    return {"Message": "User has been created successfully", "user_id": user_id}

@router.post("/login", status_code=200)
async def login_user(user: UserLogin):
    cond = await get_user(user.email)
    if not cond:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with the email does not exist")
    hashed_password = cond["password"]
    # password=get_pwd(user.password)
    if not verify_password(user.password,hashed_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")
    
    token = create_token(cond["id"])
    return {"Message": "User has been logged in successfully",
                    "token": "Bearer " + token}