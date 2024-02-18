from sqlalchemy import TIMESTAMP, Column, Integer, String, text, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Post(Base):
    __tablename__ = "posts1"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    author = Column(String)
    publisher = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey ("users1.id", ondelete="CASCADE"), nullable = False)
    
    owner = relationship("User")
    
class User(Base):
    __tablename__ = "users1"
    
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable= False)
    password = Column(String, nullable= False)
    created_at = Column(TIMESTAMP(timezone=True), nullable= False, server_default=text('now()'))
    phone_number = Column(String)

class Vote(Base):
    __tablename__ = "votes"
    post_id = Column(Integer, ForeignKey ("posts1.id", ondelete="CASCADE"), primary_key = True)
    user_id = Column(Integer, ForeignKey ("users1.id", ondelete="CASCADE"), primary_key = True)
