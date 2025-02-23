from sqlalchemy.orm import Session
from app.models.models import HotelModel
from app.schemas.schemas import *
from fastapi import HTTPException,status
from typing import List
from app.models.models import *
from fastapi import Depends
from sqlalchemy import and_

def create_booking_line(booking_schema:BookingLineBase,db:Session):    
   
    db_booking=BookingLineModel(
    room_id=booking_schema.room_id,
    booking_id=booking_schema.booking_id
    )
 
    try:
        db.add(db_booking)
        db.commit()
        db.refresh(db_booking)
        return db_booking
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

def get_all_booking_lines(db:Session)-> List[BookingLineModel]:       
    try:
       return db.query(BookingLineModel).all()
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

def get_my_all_booking_lines(user:UserModel,db:Session):
    try:
        return db.query(BookingLineModel).join(BookingModel,BookingModel.user_id==user.id).all()
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

def get_booking_line_by_id(id:int,db:Session,user:UserModel):    
    booking=db.query(BookingLineModel).join(BookingModel,BookingLineModel.booking_id==BookingModel.id).filter(and_(BookingLineModel.id==id,BookingModel.user_id==user.id)).first()
    if booking is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No such an object")
    return booking

def delete_booking_line_by_id(id:int,db:Session,user:UserModel):  
    existing_booking_line=db.query(BookingLineModel).join(BookingModel,BookingLineModel.id==id).filter(BookingModel.user_id==user.id).first()
    if existing_booking_line is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="There is no such an object.")
    try:
        db.delete(existing_booking_line)
        db.commit()
        db.refresh(existing_booking_line)
        return existing_booking_line
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
    