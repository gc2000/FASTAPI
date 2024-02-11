from fastapi import Depends, FastAPI, Response, HTTPException, status
from fastapi.params import Body
import psycopg2, time
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from . import models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)



app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@app.get("/posts/",  response_model= list[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts


@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model= schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@app.get("/posts/{id}", response_model= schemas.Post)
def get_post_by_id(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    return post

@app.delete("/posts/{id}")
def delete_post_by_id(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    
    if post.first() is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Record id {id} is not found")
    
    post.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}",  response_model= schemas.Post)
def update_post_by_id(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Record id {id} is not found")
    
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    
    return post_query.first()