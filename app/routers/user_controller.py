from fastapi import APIRouter,Depends
from app.schemas.user_schema import UserSchema
from app.database import get_db
from sqlalchemy.orm.session import Session
from app.database_services import user_database_service

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/")
def create_user(user: UserSchema,db:Session=Depends(get_db)):
    user_database_service.create_user(user,db)