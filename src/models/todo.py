from typing import Optional
from pydantic import BaseModel, ConfigDict

class TodoIn(BaseModel):
    """TodoIn model definition"""
    task: str
    user_id: Optional[int] = int

class Todo(TodoIn):
    """Todo model definition"""
    model_config = ConfigDict(from_attributes=True)
    id: int