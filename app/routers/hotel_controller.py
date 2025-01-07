from fastapi import APIRouter,Body,Depends
from sqlalchemy.orm.session import Session
from app.services.database_service import get_db
from app.schemas.schemas import HotelBase
from app.database_services import hotel_database_service
from app.schemas.schemas import *
from typing import List

router=APIRouter(prefix="/hotels",tags=["hotel"]) 

#post
@router.post("")
def create_hotel(hotel_schema:HotelBase,db:Session=Depends(get_db)):
    hotel_database_service.create_hotel(hotel_schema,db)
    return 1

#get
@router.get("",response_model= List[HotelDisplay])
def get_all_hotels(db:Session=Depends(get_db)):
    return hotel_database_service.get_all_hotels(db)

@router.get("/{id}")
def get_hotel_by_id(id:int,db:Session=Depends(get_db)):
   return hotel_database_service.get_hotel_by_id(id,db)
    
#delete
@router.delete("/{id}")
def delete_hotel_by_id(id:int,db:Session=Depends(get_db)):
    hotel_database_service.delete_hotel_by_id(id,db)
    return 1

#update
@router.put
def update_hotel(hotel_update:HotelUpdateBase,db: Session=Depends(get_db)):
    hotel_database_service.update_hotel(hotel_update,db)
    return 1