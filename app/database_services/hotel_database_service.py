from sqlalchemy.orm import Session
from app.models.models import HotelModel
from app.schemas.schemas import *
from fastapi import HTTPException,status
from typing import List

def create_hotel(hotel_schema:HotelBase,db:Session)-> bool:    
    db_hotel=HotelModel(
    hotel_name=hotel_schema.hotel_name,
    description=hotel_schema.description,
    adress=hotel_schema.adress,
    user_id=hotel_schema.user_id
    )
    try:
        db.add(db_hotel)
        db.commit()
        db.refresh(db_hotel)
        return True
    except:
        return False

def get_all_hotels(db:Session)-> List[HotelModel]:       
   return db.query(HotelModel).all()

def get_hotel_by_id(id:int,db:Session)->HotelModel:    
    hotel=db.query(HotelModel).filter(HotelModel.id==id).first()
    if hotel is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no such an object")
    return hotel

def delete_hotel_by_id(id:int,db:Session)-> bool:  
    db_hotel=db.query(HotelModel).filter(HotelModel.id==id).first()
    if db_hotel is None:
        return Exception()
    try:
        db.delete(db_hotel)
        db.commit()
        return True
    except:
        return False
    
def update_hotel(hotel:HotelUpdateBase,db: Session)->bool:
    pass
