from sqlalchemy import Column,ForeignKey,String,Integer
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base() 

class User(Base):
    __tablename__='user'
    id=Column('id',Integer,primary_key=True,autoincrement=True)
    username=Column('username',String)
    password=Column('password',String)
    blogs=relationship('Blog',back_populates='user')
    posts=relationship('Post',back_populates='user')
    
class Blog(Base):
    __tablename__='blog'
    id=Column('id',Integer,primary_key=True)
    title=Column('title',String)
    description=Column('description',String)
    blog_owner=Column('blog_owner',Integer,ForeignKey('user.id'))
    user=relationship('User',back_populates='blogs')
    posts=relationship('Post',back_populates='blog')
    
class Post(Base):
    __tablename__='post'
    id=Column('id',Integer,primary_key=True)
    description=Column('description',String)
    post_owner=Column('post_owner',Integer,ForeignKey('user.id'))
    blog_id=Column('blog_id',Integer,ForeignKey('blog.id'))
    user=relationship('User',back_populates='posts')
    blog=relationship('Blog',back_populates='posts')
    
    