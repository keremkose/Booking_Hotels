from fastapi import APIRouter,Body,Depends
from sqlalchemy.orm.session import Session
from app.services.database_service import get_db
from app.database_services import user_rating_database_service
from app.schemas.schemas import *
from typing import List
from app.models.models import *
from fastapi import Depends
from app.services.oauth2_service import get_current_user

router=APIRouter(prefix="/user_ratings",tags=["user_rating"]) 

#post
@router.post("",response_model=UserRatingDisplay)
def create_user_rating(user_rating_schema:UserRatingBase,db:Session=Depends(get_db),user:UserModel=Depends(get_current_user)):
    return user_rating_database_service.create_user_rating(user,user_rating_schema,db)
     
#get
@router.get("",response_model= List[UserRatingDisplay])
def get_all_user_ratings(db:Session=Depends(get_db),user:UserModel=Depends(get_current_user)):
    return user_rating_database_service.get_all_user_ratings(db,user)

@router.get("",response_model= List[UserRatingDisplay])
def get_my_all_user_ratings(db:Session=Depends(get_db),user:UserModel=Depends(get_current_user)):
    return user_rating_database_service.get_my_all_user_ratings(user,db)

@router.get("/{id}")
def get_user_rating_by_id(id:int,db:Session=Depends(get_db),user:UserModel=Depends(get_current_user)):
   return user_rating_database_service.get_user_rating_by_id(id,db)
    
#delete
@router.delete("/{id}")
def delete_user_rating_by_id(id:int,db:Session=Depends(get_db),user=Depends(get_current_user)):
    user_rating_database_service.delete_user_rating_by_id(id,db,user)

#update
@router.put("")
def update_user_rating(user_rating_update:UserRatingUpdateBase=Body(),db: Session=Depends(get_db),user=Depends(get_current_user)):
    return user_rating_database_service.update_user_rating(user_rating_update,db,user)
     