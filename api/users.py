from fastapi import APIRouter,Depends,HTTPException,status
from secure import get_current_active_user,get_current_user,get_password_hash,create_access_token,authenticate_user
from datetime import timedelta,timezone
from fastapi.security import OAuth2PasswordRequestForm
from models.schemas import Token,TokenData,UserCreate,UserList
from sqlalchemy.orm import Session
from models.sqlmodels import User 
from db import connect 
user_router=APIRouter()

@user_router.post('/new/user')
async def create_new_user(req:UserCreate,db:Session=Depends(connect)):
    user_db=db.query(User).filter(User.username==req.username).first()
    if user_db:
        raise HTTPException(detail='username already exist',status_code=401)
    user_db=User(**req.dict())
    user_db.password=get_password_hash(req.password)
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db


@user_router.post('/token')
async def login_for_access_token(
    form_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(connect)
) -> Token:
    user = authenticate_user(form_data.username, form_data.password,db=db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@user_router.get('/users/all',response_model=list[UserList])
async def get_all_users(db:Session=Depends(connect)):
    return db.query(User).all() 

@user_router.get('/user/{id}')
async def get_one_user(id:int,db:Session=Depends(connect)):
    return db.query(User).filter(User.id==id).first()


@user_router.get("/users/me/")
async def read_users_me(
    current_user: User=Depends(get_current_active_user),
):
    return current_user


