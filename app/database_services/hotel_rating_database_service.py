from sqlalchemy.orm import Session
from app.schemas.schemas import *
from fastapi import HTTPException,status
from typing import List
from app.models.models import *
from fastapi import Depends
from sqlalchemy import and_

def create_hotel_rating(current_user:UserModel,hotel_rating_schema:HotelRatingBase,db:Session):    
    existing_hotel_rating=db.query(HotelRatingModel).join(HotelModel,HotelRatingModel.hotel_id==HotelModel.id).first()
    if existing_hotel_rating is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Hotel rating with this name already exists.")
    
    db_hotel_rating=HotelRatingModel(
    rate=hotel_rating_schema.rate,
    review=hotel_rating_schema.review,
    hotel_id=hotel_rating_schema.user_id,
    user_id=current_user.id
    )
 
    try:
        db.add(db_hotel_rating)
        db.commit()
        db.refresh(db_hotel_rating)
        return db_hotel_rating
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

def get_all_hotel_ratings(db:Session)-> List[HotelRatingModel]:       
    try:
       return db.query(HotelRatingModel).all()
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

def get_my_all_hotel_ratings(user:UserModel,db:Session,hotel_id:int):
    try:
        return db.query(HotelRatingModel).filter(and_(HotelRatingModel.user_id==user.id,HotelRatingModel.hotel_id==hotel_id)).all()
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

def get_hotel_rating_by_id(id:int,db:Session,user:UserModel):    
    hotel_rating=db.query(HotelRatingModel).filter(and_(HotelRatingModel.id==id,HotelRatingModel.user_id==user.id)).first()
    if hotel_rating is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No such an object")
    return hotel_rating

def delete_hotel_rating_by_id(id:int,db:Session,user:UserModel):  
    db_hotel_rating=db.query(HotelRatingModel).filter(and_(HotelRatingModel.id==id,HotelRatingModel.user_id==user.id)).first()
    if db_hotel_rating is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="There is no such an object.")
    try:
        db.delete(db_hotel_rating)
        db.commit()
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
    
def update_hotel_rating(hotel_rating_update:HotelRatingUpdateBase,db: Session,user:UserModel):
    db_hotel_rating=db.query(HotelRatingModel).filter(and_(HotelRatingModel.id==hotel_rating_update.id,HotelRatingModel.user_id==user.id)).first()
    if db_hotel_rating is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="There is no such an object.")
    try:
        for field, value in hotel_rating_update.dict(exclude_unset=True).items():
            setattr(db_hotel_rating,field,value)
        db.commit()
        db.refresh(db_hotel_rating)
        return db_hotel_rating
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
