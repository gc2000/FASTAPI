from fastapi import Depends, FastAPI, Response, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(
    prefix= "/user",
    tags = ["Users"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model= schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    
    #hash password
    hashed_password = utils.hash(user.password)

    user.password = hashed_password
    
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/",  response_model= list[schemas.User])
def get_users(db: Session = Depends(get_db)):
    user = db.query(models.User).all()
    return user


@router.get("/{id}", response_model= schemas.User)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Record id {id} is not found")
    return user

@router.delete("/{id}")
def delete_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    
    if user.first() is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Record id {id} is not found")
    
    user.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}",  response_model= schemas.UserResponse)
def update_post_by_id(id: int, updated_user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hash(updated_user.password)
    updated_user.password = hashed_password
    user_query = db.query(models.User).filter(models.User.id == id)
    user = user_query.first()
    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Record id {id} is not found")
    
    user_query.update(updated_user.dict(), synchronize_session=False)
    db.commit()
    
    return user_query.first()

