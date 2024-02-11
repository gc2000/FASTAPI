from sqlalchemy import TIMESTAMP, Column, Integer, String, text
from .database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    author = Column(String)
    publisher = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable= False)
    password = Column(String, nullable= False,)
    created_at = Column(TIMESTAMP(timezone=True), nullable= False, server_default=text('now()'))
