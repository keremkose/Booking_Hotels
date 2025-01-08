from fastapi import APIRouter,Body,Depends
from sqlalchemy.orm.session import Session
from app.services.database_service import get_db
from app.schemas.schemas import BookingBase
from app.database_services import booking_database_service
from app.schemas.schemas import *
from typing import List
from app.models.models import *
from fastapi import Depends
from app.services.oauth2_service import get_current_user

router=APIRouter(prefix="/bookings",tags=["booking"]) 
#post
@router.post("",response_model=BookingDisplay)
def create_booking(booking_schema:BookingBase,db:Session=Depends(get_db),user:BookingModel=Depends(get_current_user)):
    return booking_database_service.create_booking(user.id,booking_schema,db)
     
#get
@router.get("",response_model= List[BookingDisplay])
def get_all_bookings(db:Session=Depends(get_db)):
    return booking_database_service.get_all_bookings(db)

@router.get("",response_model= List[BookingDisplay])
def get_my_all_bookings(db:Session=Depends(get_db),user:BookingModel=Depends(get_current_user)):
    return booking_database_service.get_my_all_bookings(user,db)

@router.get("/{id}")
def get_booking_by_id(id:int,db:Session=Depends(get_db),user:BookingModel=Depends(get_current_user)):
   return booking_database_service.get_booking_by_id(id,db,user)
    
#delete
@router.delete("/{id}")
def delete_bookings_by_id(id:int,db:Session=Depends(get_db),user=Depends(get_current_user)):
    booking_database_service.delete_booking_by_id(id,db,user)

#update
@router.put("",response_model=BookingDisplay)
def update_bookings(booking_update:BookingUpdateBase=Body(),db: Session=Depends(get_db),user=Depends(get_current_user)):
    return booking_database_service.update_booking(booking_update,db,user)
     