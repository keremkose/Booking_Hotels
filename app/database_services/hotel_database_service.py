from sqlalchemy.orm.session import Session
from app.models.models import HotelModel
from app.schemas.schemas import HotelBase


def create_hotel(hotel_schema:HotelBase,db:Session):    
    db_hotel=HotelModel(
    hotel_name=hotel_schema.hotel_name,
    description=hotel_schema.description,
    adress=hotel_schema.adress,
    user_id=hotel_schema.user_id
    )
    db.add(db_hotel)
    db.commit()
    db.refresh(db_hotel)
    return 1

def get_all_hotels(db:Session):       
   return db.query(HotelModel).all()

def get_hotel_by_id(id:int,db:Session):       
    return db.query(HotelModel).filter(HotelModel.id==id).first()

def delete_hotel_by_id(id:int,db:Session):  
    db_hotel=db.query(HotelModel).filter(HotelModel.id==id).first()
    if db_hotel is None:
        return Exception()
    db.delete(db_hotel)
    db.commit()
    return 1

