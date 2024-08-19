from fastapi import Depends,APIRouter,status
from models import schemas,sqlmodels
from repository.posts import create_post,get_posts,get_post
from sqlalchemy.orm import Session
from db import connect 

post_router=APIRouter()


@post_router.post('/new/post')
def create_new_post(req:schemas.PostCreate,blog_id:int,post_owner:int,db:Session=Depends(connect)):
    blog=create_post(req=req,post_owner=post_owner,blog_id=blog_id,db=db)
    return blog

@post_router.get('/all/postss',response_model=list[schemas.PostList])
def get_all_posts(db:Session=Depends(connect)):
    blogs=get_posts(db=db)
    return blogs 

@post_router.get('/post/{id}',response_model=schemas.PostList)
def get_one_post(id:int,db:Session=Depends(connect)):
    blog=get_post(id=id,db=db)
    return blog 