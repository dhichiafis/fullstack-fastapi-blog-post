from fastapi import Depends,APIRouter,status
from models import schemas,sqlmodels
from repository.blogs import create_blog,get_blogs,get_blog,get_user_blog
from sqlalchemy.orm import Session
from db import connect 

blog_router=APIRouter()


@blog_router.post('/new/blog',response_model=schemas.BlogList)
async def create_new_blog(req:schemas.BlogCreate,blog_owner:int,db:Session=Depends(connect)):
    blog=create_blog(req=req,blog_owner=blog_owner,db=db)
    return blog

@blog_router.get('/all/blogs',response_model=list[schemas.BlogList])
async def get_all_blogs(db:Session=Depends(connect)):
    blogs=get_blogs(db=db)
    return blogs 

@blog_router.get('/blog/{id}')
async def get_one_blog(id:int,db:Session=Depends(connect)):
    blog=get_blog(id=id,db=db)
    return blog 

@blog_router.get('/blog/{id}')
async def get_one_blog(id:int,db:Session=Depends(connect)):
    blog=get_blog(id=id,db=db)
    return blog 

@blog_router.get('/blog/user/{blog_owner}')
async def get_blog_user(blog_owner:int,db:Session=Depends(connect)):
    blogs=get_user_blog(blog_owner=blog_owner,db=db)
    return blogs