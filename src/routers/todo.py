from fastapi import APIRouter, Depends, HTTPException

from models.todo import TodoIn
from database.config import database, todo_table
from utils.security import get_current_user, get_current_user_id

router = APIRouter(dependencies=[Depends(get_current_user)])

@router.get("/")
async def index():
    return {"message": "Hello, World!"}

@router.get("/check-task", status_code=200)
async def check_tasks():
    query = todo_table.select()
    return await database.fetch_all(query)

@router.post("/create-task", status_code=201)
async def create_task(todo: TodoIn, user_id:int = Depends(get_current_user_id)):
    query = todo_table.insert().values(task=todo.task, user_id= user_id)
    last_record_id = await database.execute(query)
    return {"task":todo.task, "id": last_record_id}

@router.put("/update-task/{task_id}", status_code=200)
async def update_task(task_id: int, todo: TodoIn ,user_id:int = Depends(get_current_user_id)):
    query = todo_table.update().where(todo_table.c.id == task_id).values(task=todo.task, user_id=user_id)
    await database.execute(query)
    return {"message": f"Task with id: {task_id} has been updated"}

@router.delete("/delete-task/{task_id}", status_code=200)
async def delete_task(task_id: int,user_id:int = Depends(get_current_user_id)):
    query = todo_table.select().where(todo_table.c.id == task_id)
    task = await database.fetch_one(query)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this task")

    delete_query = todo_table.delete().where(todo_table.c.id == task_id)
    await database.execute(delete_query)
    return {"message": f"Task with id: {task_id} has been deleted"}

