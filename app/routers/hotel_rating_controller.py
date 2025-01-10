from fastapi import APIRouter,Body,Depends
from sqlalchemy.orm.session import Session
from app.services.database_service import get_db
from app.database_services import hotel_rating_database_service
from app.schemas.schemas import *
from typing import List
from app.models.models import *
from fastapi import Depends
from app.services.oauth2_service import get_current_user

router=APIRouter(prefix="/hotel_ratings",tags=["hotel_ratings"]) 

#post
@router.post("",response_model=HotelRatingDisplay)
def create_hotel_rating(hotel_rating_schema:HotelRatingBase,db:Session=Depends(get_db),user:UserModel=Depends(get_current_user)):
    return hotel_rating_database_service.create_hotel_rating(user,hotel_rating_schema,db)
     
#get
@router.get("")
def get_all_hotel_ratings(db:Session=Depends(get_db),user:UserModel=Depends(get_current_user)):
    return hotel_rating_database_service.get_all_hotel_ratings(db,user)

@router.get("/{hotel_id}",response_model= List[HotelRatingDisplay])
def get_my_all_hotel_ratings(hotel_id:int,db:Session=Depends(get_db),user:UserModel=Depends(get_current_user)):
    return hotel_rating_database_service.get_my_all_hotel_ratings(user,db,hotel_id)

@router.get("/{id}")
def get_hotel_rating_by_id(id:int,db:Session=Depends(get_db)):
   return hotel_rating_database_service.get_hotel_rating_by_id(id,db)
    
#delete
@router.delete("/{id}")
def delete_hotel_rating_by_id(id:int,db:Session=Depends(get_db),user=Depends(get_current_user)):
    hotel_rating_database_service.delete_hotel_rating_by_id(id,db,user)

#update
@router.put("",response_model=HotelRatingDisplay)
def update_hotel_rating(hotel_rating_update:HotelRatingUpdateBase=Body(),db: Session=Depends(get_db),user=Depends(get_current_user)):
    return hotel_rating_database_service.update_hotel_rating(hotel_rating_update,db,user)
     