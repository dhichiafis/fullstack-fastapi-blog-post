from fastapi import FastAPI 
from db import engine
import uvicorn 
from api.users import user_router
from api.blogs import blog_router 
from api.posts import post_router
import models
from fastapi.middleware.cors import CORSMiddleware
origins=['http://localhost:5173','http://localhost:8900']

app=FastAPI()
app.add_middleware(
    CORSMiddleware,allow_origins=origins,allow_headers=["*"],allow_methods=["*"],allow_credentials=True
)
models.sqlmodels.Base.metadata.create_all(bind=engine)
app.include_router(user_router,prefix='/users')
app.include_router(blog_router,prefix='/blogs')
app.include_router(post_router,prefix='/posts')

if __name__=="__main__":
    uvicorn.run("main:app",reload=True,host='127.0.0.1',port=8900)