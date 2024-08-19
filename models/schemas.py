from pydantic import BaseModel
from typing import List
class PostCreate(BaseModel):
    description:str 
    
class PostList(PostCreate):
    
    id:int 
    blog_id:int
    post_owner:int 
    class Config:
        orm_mode=True 
        arbitrary_types_allowed=True 
        
        
class BlogCreate(BaseModel):
    title:str 
    description:str 
    
class BlogList(BlogCreate):
    id:int 
    blog_owner:int
    posts:List[PostList]
    class Config:
        orm_mode=True 
        arbitrary_types_allowed=True 
 
class UserCreate(BaseModel):
    username:str 
    password:str 
    
    
class UserList(UserCreate):
    id:int 
    blogs:List[BlogList]
    posts:List[PostList]
    class Config:
        orm_mode=True 
        arbitrary_types_allowed=True 
        

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


