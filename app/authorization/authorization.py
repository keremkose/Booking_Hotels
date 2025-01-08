from sqlalchemy.orm.session import Session
from app.models.models import UserModel
from app.schemas.schemas import *
from fastapi import HTTPException,status
from app.models.models import *

class Authorize():
    
    def is_admin(user:UserModel)-> bool:
        if user.is_admin is False:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="You are not authorized.")
        return True
