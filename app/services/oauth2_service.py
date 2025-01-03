from fastapi import Depends,HTTPException,status
from sqlalchemy.orm.session import Session
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt
from jose.exceptions import JWTError
from app.services.database_service import get_db 
from app.database_services import user_database_service 


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
 
SECRET_KEY = '142A4D41B85D0C5F6C7581EA673DDD3E426777502B86A9CEA80F0692A90B1778'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 60
 
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.now() + expires_delta
  else:
    expire = datetime.now() + timedelta(minutes=15)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt

def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):
  credential_exception=HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Couldn't validate credentials",
    headers={"WWW-Authenticate":"Bearer"}
    )
  try:
    payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    id:str=payload.get("sub")
    if id is None:
      raise credential_exception
  except JWTError:
    raise credential_exception
  user=user_database_service.get_user_by_userid(id,db)
  if user is None:
    raise credential_exception
  return user