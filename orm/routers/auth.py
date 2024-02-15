from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models, schemas, utils, oauth2
from ..database import get_db


router = APIRouter(tags= ['Authentication'])

@router.post('/login')
def login(user_credential: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credential.username).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"{user_credential.email} not found")
    
    if not utils.verify_password(user_credential.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Wrong credential")
    
    access_token = oauth2.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}