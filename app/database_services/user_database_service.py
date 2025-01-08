from app.schemas.schemas import *
from app.models.models import *
from sqlalchemy.orm.session import Session
from app.database_services.hash import Hash
from fastapi import HTTPException,status
from app.exceptions.user_exceptions import UserNotFound
from fastapi.responses import HTMLResponse
from fastapi.responses import Response

def create_user(user_schema:UserBase,db:Session):
   existing_user_email=db.query(UserModel).filter(UserModel.email==user_schema.email).first()
   existing_user_username=db.query(UserModel).filter(UserModel.username==user_schema.username).first()

   if existing_user_email or existing_user_username is not None:
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
   db_user=UserModel(
    name= user_schema.name,
    surname=user_schema.surname,
    username=user_schema.username,
    email=user_schema.email,
    password=Hash.bcrypt(user_schema.password)
   )
   db.add(db_user)
   db.commit()
   db.refresh(db_user)

   return db_user

def get_all_users(db:Session):
   try:
      return db.query(UserModel).all()
   except:
      raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
   

def get_user_by_id(id:str,db:Session):
   return db.query(UserModel).filter(UserModel.id==id).first()

#TODO delete it 
def admin_delete_user_by_id(id:int,db:Session,user:UserModel):
   if user.is_admin is False:
      raise HTTPException(status.HTTP_401_UNAUTHORIZED)
   try:
      hotels= db.query(HotelModel).filter(HotelModel.user_id==id)
      if hotels is not None:
         hotels.delete()
         db.commit()
         
      db_user=db.query(UserModel).filter(UserModel.id==id).first()
      if not db_user :
        raise UserNotFound()
   
   except UserNotFound as e:
      return f"Error: {str(e)}"
   db.delete(db_user)
   db.commit()
   return 1

def delete_user_by_id(user:UserModel,db:Session):  
  db.query(UserModel).filter(UserModel.id==user.id).filter().delete(user)
  db.commit()

def update_user_by_id(user:UserModel,user_update: UserUpdateBase, db: Session):
   db_user = db.query(UserModel).filter(UserModel.id == user.id).first()
   if db_user:
      for field, value in user_update.dict(exclude_unset=True).items():
         if field =='password' and value is not None:
            hashed_password=Hash.bcrypt(value)
            setattr(db_user,field,hashed_password)
         else :setattr(db_user, field, value)
         
      db.commit()  
      db.refresh(db_user)  
      return db_user
   else:
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"User with username {user_update.username} not found")