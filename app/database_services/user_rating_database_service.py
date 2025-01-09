from sqlalchemy.orm import Session
from app.schemas.schemas import *
from fastapi import HTTPException,status
from typing import List
from app.models.models import *
from fastapi import Depends
from sqlalchemy import and_
from app.authorization.authorization import Authorize


def create_user_rating(user:UserModel,user_rating_schema:UserRatingBase,db:Session):
    has_been_reviewd=db.query(UserRatingModel).filter(UserRatingModel.id==user.id)
    
    if has_been_reviewd is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="This is already reviewed.")    

    db_user_rating=UserRatingModel(
    manager_user_id=user_rating_schema.manager_user_id,
    customer_user_id=user_rating_schema.customer_user_id,
    rate=user_rating_schema.rate,
    comment=user_rating_schema.comment
    )
 
    try:
        db.add(db_user_rating)
        db.commit()
        db.refresh(db_user_rating)
        return db_user_rating
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

def get_all_user_ratings(db:Session,user: UserModel)-> List[UserRatingModel]:       
    try:
        if user.is_admin is True:
            return db.query(UserRatingModel).all()
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

def get_my_all_user_ratings(user:UserModel,db:Session):
    try:
        return db.query(UserRatingModel).filter(UserRatingModel.manager_user_id==user.id).all()
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

def get_user_rating_by_id(id:int,db:Session,user: UserModel):    
    user_rating_by_id=db.query(UserRatingModel).filter(and_(UserRatingModel.id==id,UserRatingModel.manager_user_id==user.id)).first()
    if user_rating_by_id is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No such an object")
    return user_rating_by_id

def delete_user_rating_by_id(id:int,db:Session,user:UserModel):  
    Authorize.is_admin()
    db_user_rating=db.query(UserRatingModel).filter(and_(UserRatingModel.id==id)).first()
    try:
        db.delete(db_user_rating)
        db.commit()
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
    
def update_user_rating(user_rating_update:UserRatingUpdateBase,db: Session,user:UserModel):
    Authorize.is_admin()    
    db_user_rating=db.query(UserRatingModel).filter(UserRatingModel.id==user_rating_update.id).first()
    
    if db_user_rating is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="There is no such an object.")
    try:
        for field, value in user_rating_update.dict(exclude_unset=True).items():
            setattr(db_user_rating,field,value)
        db.commit()
        db.refresh(db_user_rating)
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
