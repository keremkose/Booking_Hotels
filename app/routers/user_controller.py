from fastapi import APIRouter,Depends,Body,Header,Cookie,Form,Response,Request
from app.schemas.schemas import *
from app.services.database_service import get_db
from sqlalchemy.orm.session import Session
from app.database_services import user_database_service
from typing import Optional,List
from fastapi.responses import HTMLResponse
from app.services.oauth2_service import oauth2_scheme
from app.services.oauth2_service import get_current_user

router = APIRouter(prefix="/users", tags=["user"])


@router.post("")
def create_user(user: UserBase=Body(),db:Session=Depends(get_db)):
    user_database_service.create_user(user,db)

@router.get("")
def get_all_users(db:Session=Depends(get_db),user=Depends(get_current_user)):
   return {
   "users":user_database_service.get_all_users(db),
   "user":user
   }

@router.get("/{id}")
def get_user_by_id(id:int,db:Session=Depends(get_db)):
   return user_database_service.get_user_by_id(id,db)

@router.delete("/{id}")
def admin_delete_user_by_id(id:int,db:Session=Depends(get_db)):
   return user_database_service.admin_delete_user_by_id(id,db)

@router.delete("")
def delete_user_by_id(user=Depends(get_current_user),db:Session=Depends(get_db)):
   return user_database_service.delete_user_by_id(user,db)

@router.put("/{id}")
def update_user_by_id(user_update:UserUpdateBase,db:Session=Depends(get_db)):
   return user_database_service.update_user_by_id(user_update,db)

