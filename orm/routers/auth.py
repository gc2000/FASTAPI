from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db


router = APIRouter(tags= ['Authentication'])

@router.post('/login')
def login(user_credential: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credential.email).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{user_credential.email} not found")
    
    if not utils.verify_password(user_credential.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Wrong credential")
    
    return {"msg": "success"}