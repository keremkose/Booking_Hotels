from app.schemas.schemas import *
from app.models.models import *
from sqlalchemy.orm.session import Session
from app.database_services.hash import Hash
from fastapi import HTTPException,status
from app.exceptions.user_exceptions import UserNotFound
from fastapi.responses import HTMLResponse

def create_user(user_schema:UserBase,db:Session):
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
   return db.query(UserModel).all()

def get_user_by_id(id:str,db:Session):
   return db.query(UserModel).filter(UserModel.id==id).first()

def admin_delete_user_by_id(id:int,db:Session):
   #TODO should be looked at and arranged
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
  return 1
  

def update_user_by_id(user_update: UserUpdateBase, db: Session):
   db_user = db.query(UserModel).filter(UserModel.email == user_update.email).first()

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
      raise ValueError(f"User with username {user_update.username} not found")