from sqlalchemy import  Column,ForeignKey
from app.database import Base,engine
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import String,Integer,Boolean


Base.metadata.create_all(bind=engine)

class UserModel(Base):
    __tablename__="Users"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    surname=Column(String)
    username=Column(String,unique=True)
    email=Column(String,unique=True)  
    password=Column(String)


