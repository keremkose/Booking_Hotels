from fastapi import APIRouter,Body,Depends
from sqlalchemy.orm.session import Session
from app.services.database_service import get_db
from app.database_services import booking_line_database_service
from app.schemas.schemas import *
from typing import List
from app.models.models import *
from fastapi import Depends
from app.services.oauth2_service import get_current_user

router=APIRouter(prefix="/booking_lines",tags=["booking_lines"]) 
#post
@router.post("",response_model=BookingLineDisplay)
def create_booking_line(booking_line_schema:BookingLineBase,db:Session=Depends(get_db),user:BookingLineModel=Depends(get_current_user)):
    return booking_line_database_service.create_booking_line(user.id,booking_line_schema,db)
     
#get
@router.get("",response_model= List[BookingLineDisplay])
def get_all_booking_lines(db:Session=Depends(get_db)):
    return booking_line_database_service.get_all_booking_lines(db)

@router.get("",response_model= List[BookingLineDisplay])
def get_my_all_booking_lines(db:Session=Depends(get_db),user:BookingLineModel=Depends(get_current_user)):
    return booking_line_database_service.get_my_all_booking_lines(user,db)

@router.get("/{id}")
def get_booking_line_by_id(id:int,db:Session=Depends(get_db)):
   return booking_line_database_service.get_booking_line_by_id(id,db)
    
#delete
@router.delete("/{id}")
def delete_booking_line_by_id(id:int,db:Session=Depends(get_db),user=Depends(get_current_user)):
    booking_line_database_service.delete_booking_line_by_id(id,db,user)

#update
@router.put("")
def update_booking_line(booking_line_update:BookingLineUpdateBase=Body(),db: Session=Depends(get_db),user=Depends(get_current_user)):
    return booking_line_database_service.update_booking_line(booking_line_update,db,user)
     