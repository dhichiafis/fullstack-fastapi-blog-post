from sqlalchemy.orm import Session

from models import schemas,sqlmodels 


def create_post(req:schemas.PostCreate,blog_id:int,post_owner,db:Session):
    blog=sqlmodels.Post(**req.dict(),post_owner=post_owner,blog_id=blog_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog 

def get_posts(db:Session):
    return db.query(sqlmodels.Post).all()

def get_post(id:int,db:Session):
    return db.query(sqlmodels.Post).filter(sqlmodels.Post.id==id).first()
