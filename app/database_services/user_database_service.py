from app.schemas.schemas import UserBase
from app.models.models import UserModel
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

def get_user_by_username(username:str,db:Session):
   return db.query(UserModel).filter(UserModel.username==username).first()

def delete_user_by_id(id:int,db:Session):  
   try:
      db_user=db.query(UserModel).filter(UserModel.id==id).first()
      if not db_user :
        raise UserNotFound()
   
   except UserNotFound as e:
      return f"Error: {str(e)}"

   db.delete(db_user)
   db.commit()
   return 1

