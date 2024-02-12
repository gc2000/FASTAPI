from pydantic import BaseModel, EmailStr
from datetime import datetime

class PostBase (BaseModel):
    title: str
    content: str
    author: str
    publisher: str
    
class PostCreate (PostBase):
    pass    

class Post (PostBase):
    id: int
    created_at: datetime
    class Config:
        # orm_mode = True
        from_attributes = True
        
class UserCreate (BaseModel):
    email: EmailStr
    password: str
    
class User (UserCreate):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

class UserResponse (BaseModel):
    id: int
    email: EmailStr
    password: str
    created_at: datetime


class UserLogin(BaseModel):
    email: EmailStr
    password: str