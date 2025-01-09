from fastapi import APIRouter

router=APIRouter(prefix="/rooms",tags=["room"]) 

from fastapi import APIRouter,Body,Depends
from sqlalchemy.orm.session import Session
from app.services.database_service import get_db
from app.database_services import room_database_service
from app.schemas.schemas import *
from typing import List
from app.models.models import *
from fastapi import Depends
from app.services.oauth2_service import get_current_user

router=APIRouter(prefix="/room_models",tags=["room_models"]) 

#post
@router.post("",response_model=RoomDisplay)
def create_room(room_schema:RoomBase,db:Session=Depends(get_db),user:UserModel=Depends(get_current_user)):
    return room_database_service.create_room(user.id,room_schema,db)
     
#get
# @router.get("",response_model= List[RoomDisplay])
# def get_all_rooms(db:Session=Depends(get_db)):
#     return room_database_service.get_all_rooms(db)

@router.get("/{hotel_id}",response_model= List[RoomDisplay])
def get_my_all_rooms(hotel_id:int,db:Session=Depends(get_db),user:UserModel=Depends(get_current_user)):
    return room_database_service.get_my_all_rooms(hotel_id,user,db)

@router.get("/{hotel_id}/{room_number}")
def get_room_by_room_number_and_hotel_id(hotel_id:int,room_number:int,db:Session=Depends(get_db),user:UserModel=Depends(get_current_user)):
   return room_database_service.get_room_by_room_number_and_hotel_id(hotel_id,room_number,db,user)
    
#delete
@router.delete("/{hotel_id}/{room_number}")
def delete_room_by_id(hotel_id:int,room_number:int,db:Session=Depends(get_db),user=Depends(get_current_user)):
    room_database_service.delete_room_by_id(hotel_id,room_number,db,user)

#update
@router.put("",response_model=RoomDisplay)
def update_room(room_update:RoomUpdateBase=Body(),db: Session=Depends(get_db),user=Depends(get_current_user)):
    return room_database_service.update_room(room_update,db,user)
     