from fastapi import APIRouter,Depends,Body
from app.schemas.schemas import UserBase
from app.database import get_db
from sqlalchemy.orm.session import Session
from app.database_services import user_database_service

router = APIRouter(prefix="/user", tags=["user"])


@router.post("")
def create_user(user: UserBase=Body(),db:Session=Depends(get_db)):
    user_database_service.create_user(user,db)

@router.get("")
def get_all_users(db:Session=Depends(get_db)):
   return user_database_service.get_all_users(db)