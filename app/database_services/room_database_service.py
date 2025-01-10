from sqlalchemy.orm import Session
from app.schemas.schemas import *
from fastapi import HTTPException,status
from typing import List
from app.models.models import *
from fastapi import Depends,Body
from sqlalchemy import and_

def create_room(current_user_id:int,room_schema:RoomBase,db:Session):    
    
    existing_room=db.query(RoomModel).join(HotelModel,RoomModel.hotel_id==HotelModel.id).filter(
        and_(RoomModel.room_number==room_schema.room_number,RoomModel.hotel_id==room_schema.hotel_id,HotelModel.user_id==current_user_id)).first()

    if existing_room is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="room with this name already exists.")
    
    db_room=RoomModel(
    room_number=room_schema.room_number,
    size=room_schema.size,
    bed_count=room_schema.bed_count,
    price_per_night=room_schema.price_per_night,
    hotel_id=room_schema.hotel_id
    )
    try:
        db.add(db_room)
        db.commit()
        db.refresh(db_room)
        return db_room
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

def get_all_rooms(db:Session)-> List[RoomModel]:       
    try:
       return db.query(RoomModel).all()
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

def get_my_all_rooms(hotel_id:int,user:UserModel,db:Session):
    try:
        return db.query(RoomModel).join(HotelModel,RoomModel.hotel_id==HotelModel.id).filter(and_(RoomModel.hotel_id==hotel_id,HotelModel.user_id==user.id)).all()
    except:
        raise HTTPException(detail="There is an issue occured.",status_code=status.HTTP_404_NOT_FOUND)

def get_room_by_room_number_and_hotel_id(hotel_id:int,room_number:int,db:Session,user:UserModel):    
    room=db.query(RoomModel).join(HotelModel,RoomModel.hotel_id==HotelModel.id).filter(and_(RoomModel.hotel_id==hotel_id,HotelModel.user_id==user.id)).first()
    if room is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No such an object")
    return room

def delete_room_by_id(hotel_id: int, room_number: int, db: Session, user: UserModel):  
    db_room = db.query(RoomModel).join(
        HotelModel, HotelModel.id == RoomModel.hotel_id
    ).filter(
        and_(
            RoomModel.hotel_id == hotel_id,
            RoomModel.room_number == room_number,
            HotelModel.user_id == user.id
        )
    ).first()

    if db_room is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no such an object."
        )

    # Verify user authorization
    if user.id != db_room.hotel.user_id:  # Assumes a relationship exists between RoomModel and HotelModel
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You are not authorized to delete this room."
        )

    try:
        db.delete(db_room)
        db.commit()
    except Exception as e:
        db.rollback()  # Rollback the transaction in case of an error
        raise HTTPException(
            detail=f"There is an issue occurred: {str(e)}",
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE
        )
def update_room(room_update: RoomUpdateBase, db: Session, user: UserModel):
    # Ensure you are using the appropriate fields from room_update
    db_room = db.query(RoomModel).join(
        HotelModel, HotelModel.id == room_update.hotel_id
    ).filter(
        and_(
            RoomModel.room_number == room_update.room_number,
            RoomModel.hotel_id == room_update.hotel_id,
            HotelModel.user_id == user.id
        )
    ).first()

    if db_room is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no such an object."
        )

    try:
        # Update the fields dynamically
        for field, value in room_update.dict(exclude_unset=True).items():
            setattr(db_room, field, value)

        db.commit()
        db.refresh(db_room)
        return db_room

    except Exception as e:
        db.rollback()  # Rollback the transaction in case of an error
        raise HTTPException(
            detail=f"There is an issue occurred: {str(e)}",
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE
        )