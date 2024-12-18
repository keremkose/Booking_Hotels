from app.schemas.schemas import UserBase
from app.models.models import UserModel
from sqlalchemy.orm.session import Session
from app.database_services.hash import Hash



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