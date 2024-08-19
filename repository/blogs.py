from sqlalchemy.orm import Session

from models import schemas,sqlmodels 


def create_blog(req:schemas.BlogCreate,blog_owner:int,db:Session):
    blog=sqlmodels.Blog(**req.dict(),blog_owner=blog_owner)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog 

def get_blogs(db:Session):
    return db.query(sqlmodels.Blog).all()

def get_blog(id:int,db:Session):
    return db.query(sqlmodels.Blog).filter(sqlmodels.Blog.id==id).first()


def get_user_blog(blog_owner:int,db:Session):
    return db.query(sqlmodels.Blog).filter(sqlmodels.Blog.blog_owner==blog_owner).all()
