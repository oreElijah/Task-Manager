from typing import Optional
from pydantic import BaseModel, ConfigDict

class UserIn(BaseModel):    
    """UserIn model definition"""
    first_name: str
    last_name: str
    middle_name: Optional[str]=None
    email: str
    password: str      

class User(UserIn):
    """User model definition"""
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int]=None

class UserLogin(BaseModel):    
    """UserLogIn model definition"""
    email: str
    password: str      
    id: Optional[int]=None
