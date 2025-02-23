from fastapi import APIRouter,Body,Depends
from sqlalchemy.orm.session import Session
from app.services.database_service import get_db
from app.schemas.schemas import HotelBase
from app.database_services import hotel_database_service
from app.schemas.schemas import *
from typing import List
from app.models.models import *
from fastapi import Depends
from app.services.oauth2_service import get_current_user

router=APIRouter(prefix="/hotels",tags=["hotel"]) 

#post
@router.post("",response_model=HotelDisplay)
def create_hotel(hotel_schema:HotelBase,db:Session=Depends(get_db),user:UserModel=Depends(get_current_user)):
    return hotel_database_service.create_hotel(user.id,hotel_schema,db)
     
#get
@router.get("",response_model= List[HotelDisplay])
def get_all_hotels(db:Session=Depends(get_db)):
    return hotel_database_service.get_all_hotels(db)

@router.get("",response_model= List[HotelDisplay])
def get_my_all_hotels(db:Session=Depends(get_db),user:UserModel=Depends(get_current_user)):
    return hotel_database_service.get_my_all_hotels(user,db)

@router.get("/with_reviews")
def get_hotels_with_reviews(db:Session=Depends(get_db)):
 return hotel_database_service.get_hotels_with_reviews(db)

@router.get("/{id}")
def get_hotel_by_id(id:int,db:Session=Depends(get_db),user:UserModel=Depends(get_current_user)):
   return hotel_database_service.get_hotel_by_id(id,db,user)
    
#delete
@router.delete("/{id}")
def delete_hotel_by_id(id:int,db:Session=Depends(get_db),user=Depends(get_current_user)):
    hotel_database_service.delete_hotel_by_id(id,db,user)

#update
@router.put("",response_model=HotelDisplay)
def update_hotel(hotel_update:HotelUpdateBase=Body(),db: Session=Depends(get_db),user=Depends(get_current_user)):
    return hotel_database_service.update_hotel(hotel_update,db,user)
     