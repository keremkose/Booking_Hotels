from fastapi import APIRouter,Depends,Body,Header,Cookie,Form,Response,Request
from app.schemas.schemas import *
from app.services.database_service import get_db
from sqlalchemy.orm.session import Session
from app.database_services import user_database_service
from typing import Optional,List
from fastapi.responses import HTMLResponse
from app.services.oauth2_service import oauth2_scheme
from app.services.oauth2_service import get_current_user
from app.models.models import *
from app.config import settings
import os
import sys

router = APIRouter(prefix="/users", tags=["user"])


@router.post("",response_model=UserDisplay)
def create_user(user: UserBase=Body(),db:Session=Depends(get_db)):
   return user_database_service.create_user(user,db)

@router.get("",response_model=List[UserDisplay])
def admin_get_all_users(user:UserModel=Depends(get_current_user),db:Session=Depends(get_db)):
   return user_database_service.get_all_users(user,db)

@router.get("/{id}")
def admin_get_user_by_id(id:int,db:Session=Depends(get_db),user:UserModel=Depends(get_current_user)):
   return user_database_service.get_user_by_id(id,db,user)

#TODO delete it
@router.delete("/{id}")
def admin_delete_user_by_id(id:int,db:Session=Depends(get_db),user:UserModel=Depends(get_current_user)):
   user_database_service.admin_delete_user_by_id(id,db,user)

@router.delete("")
def delete_user_by_id(user=Depends(get_current_user),db:Session=Depends(get_db)):
   return user_database_service.delete_user_by_id(user,db)

@router.put("/{id}",response_model=UserDisplay)
def update_user_by_id(user_update:UserUpdateBase,db:Session=Depends(get_db),user:UserModel=Depends(get_current_user)):
   return user_database_service.update_user_by_id(user,user_update,db)

