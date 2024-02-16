from typing import Optional
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime

class PostBase (BaseModel):
    title: str
    content: str
    author: str
    publisher: str
    
class PostCreate (PostBase):
    pass    


class UserResponse (BaseModel):
    id: int
    email: EmailStr
    password: str
    created_at: datetime


class Post (PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse
    
    class Config:
        # orm_mode = True
        from_attributes = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True
        # from_attributes = True
        
class UserCreate (BaseModel):
    email: EmailStr
    password: str
    
class User (UserCreate):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class Token (BaseModel):
    access_token: str
    token_type: str
    
class TokenData (BaseModel):
    id: Optional[int] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)