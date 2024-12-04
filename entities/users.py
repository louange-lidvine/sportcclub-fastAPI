# from datetime import timedelta
# from typing import Annotated
#
# from fastapi import APIRouter, Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordRequestForm
# from sqlalchemy.orm import Session
#
# from core.database import get_db
# from core import security as auth
# from core.security import verify_password, create_access_token
# from entities import models, schemas
# from services import crud
#
# router = APIRouter()
#
#
# @router.post("/users/", response_model=schemas.User)
# async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)
#
#
# @router.get("/users/me/", response_model=schemas.User)
# async def read_users_me(current_user: models.User = Depends(auth.get_current_user)):
#     return current_user
#
#
# @router.post("/login/")
# def login(user: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
#     db_user = db.query(models.User).filter(models.User.email == user.username).first()
#     print(db_user)
#     if not db_user:
#         raise HTTPException(status_code=404, detail="User not found")
#     if not verify_password(user.password, db_user.hashed_password):
#         raise HTTPException(status_code=400, detail="Invalid credentials")
#     access_token = create_access_token({"sub": db_user.email})
#     return {"access_token": access_token, "token_type": "bearer"}
#
