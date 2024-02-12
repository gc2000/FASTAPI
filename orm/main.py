from fastapi import Depends, FastAPI, Response, HTTPException, status
from fastapi.params import Body
import psycopg2, time
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import SessionLocal, engine
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)