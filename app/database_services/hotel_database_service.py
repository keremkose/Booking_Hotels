from sqlalchemy.orm import Session
from app.models.models import HotelModel
from app.schemas.schemas import *
from fastapi import HTTPException,status
from typing import List
from app.models.models import *
from fastapi import Depends

def create_hotel(current_user_id:int,hotel_schema:HotelBase,db:Session):    
    existing_hotel=db.query(HotelModel).filter(HotelModel.hotel_name==hotel_schema.hotel_name).first()

    if existing_hotel is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Hotel with this name already exists.")
    
    db_hotel=HotelModel(
    hotel_name=hotel_schema.hotel_name,
    description=hotel_schema.description,
    adress=hotel_schema.adress,
    user_id=current_user_id
    )
 
    try:
        db.add(db_hotel)
        db.commit()
        new_hotel=db.query(HotelModel).filter(HotelModel.hotel_name==hotel_schema.hotel_name).first()
        db.refresh(db_hotel)
        return new_hotel
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

def get_all_hotels(db:Session)-> List[HotelModel]:       
    try:
       return db.query(HotelModel).all()
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

def get_my_all_hotels(user:UserModel,db:Session):
    try:
        return db.query(HotelModel).filter(HotelModel.user_id==user.id).all()
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

def get_hotel_by_id(id:int,db:Session):    
    hotel=db.query(HotelModel).filter(HotelModel.id==id).first()
    if hotel is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No such an object")
    return hotel

def delete_hotel_by_id(id:int,db:Session,user:UserModel):  
    db_hotel=db.query(HotelModel).filter(HotelModel.id==id).first()
    if db_hotel is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="There is no such an object.")
    if user.id != db_hotel.user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are not authorized to delete this hotel.")
    try:
        db.delete(db_hotel)
        db.commit()
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
    
def update_hotel(hotel_update:HotelUpdateBase,db: Session,user:UserModel):
    db_hotel=db.query(HotelModel).filter(HotelModel.id==hotel_update.id).first()
    if db_hotel is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="There is no such an object.")
    if user.id != db_hotel.user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are not authorized to delete this hotel.")
    try:
        for field, value in hotel_update.dict(exclude_unset=True).items():
            setattr(db_hotel,field,value)
        db.commit()
        db.refresh(db_hotel)
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
