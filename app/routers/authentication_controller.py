from fastapi import APIRouter,HTTPException,Depends,status
from sqlalchemy.orm.session import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app.services.database_service import get_db
from app.models import models
from app.database_services.hash import Hash 
from app.services import oauth2_service 

router = APIRouter(
    tags=['authentication']
)

@router.post("/token")
def get_token(request:OAuth2PasswordRequestForm=Depends(),db:Session = Depends(get_db)):
    user=db.query(models.UserModel).filter(models.UserModel.username==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid credentials.")
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password.")
    access_token=oauth2_service.create_access_token(data={"sub":str(user.id)}) 
    
    return {
    "access_token":access_token,
    "token_type":"bearer",
    "user_id": user.id,
    "user_name":user.username
    }
