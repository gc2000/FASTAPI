from pydantic import BaseModel
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
        orm_mode = True
        # from_attributes = True
        
class UserBase (BaseModel):
    email: str
    password: str
    
class UserCreate (UserBase):
    pass    