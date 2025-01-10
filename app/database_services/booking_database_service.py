from sqlalchemy.orm import Session
from app.models.models import HotelModel
from app.schemas.schemas import *
from fastapi import HTTPException,status
from typing import List
from app.models.models import *
from fastapi import Depends
from sqlalchemy import and_
from app.authorization.authorization import Authorize

def create_booking(current_user_id:int,booking_schema:BookingBase,db:Session):    
    if booking_schema.checkin_date.day >= booking_schema.checkout_date.day: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)   
    db_booking=BookingModel(
    checkin_date=booking_schema.checkin_date,
    checkout_date=booking_schema.checkout_date,
    booking_status=False,
    user_id=current_user_id
    )
 
    try:
        db.add(db_booking)
        db.commit()
        db.refresh(db_booking)
        return db_booking
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

def get_all_bookings(user:UserModel,db:Session)-> List[BookingModel]:       
    Authorize.is_admin(user)
    try:
       return db.query(BookingModel).all()
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

def get_my_all_bookings(user:UserModel,db:Session):
    try:
        return db.query(BookingModel).filter(BookingModel.user_id==user.id).all()
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

def get_booking_by_id(id:int,db:Session,user:UserModel):    
    booking=db.query(BookingModel).filter(and_(BookingModel.id==id ,BookingModel.user_id==user.id)).first()
    if booking is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No such an object")
    return booking

def delete_booking_by_id(id:int,db:Session,user:UserModel):  
    db_booking=db.query(BookingModel).filter(BookingModel.id==id).first()
    if db_booking is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="There is no such an object.")
    if user.id != db_booking.user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are not authorized to delete this booking.")
    try:
        db.delete(db_booking)
        db.commit()
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
    
def update_booking(booking_update:BookingUpdateBase,db: Session,user:UserModel):
    db_booking=db.query(BookingModel).filter(BookingModel.id==booking_update.id).first()
    if db_booking is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="There is no such an object.")
    if user.id != db_booking.user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are not authorized to delete this booking.")
    try:
        for field, value in booking_update.dict(exclude_unset=True).items():
            setattr(db_booking,field,value)
        db.commit()
        db.refresh(db_booking)
        return db_booking
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
