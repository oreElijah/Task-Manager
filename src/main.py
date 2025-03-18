from contextlib import asynccontextmanager
from fastapi import FastAPI

from database.config import connect_db, disconnect_db
from routers.todo import router as todo_router
from routers.users import router as user_router

@asynccontextmanager
async def lifespan(app:FastAPI):
    await connect_db()
    yield
    await disconnect_db()

app = FastAPI(lifespan=lifespan)

app.include_router(todo_router, prefix="/api/v1/task")
app.include_router(user_router,  prefix="/api/v1/user")