from sqlalchemy import  Column,ForeignKey,Table
from app.services.database_service import Base,engine
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import String,Integer,Boolean,Date

class UserModel(Base):
    __tablename__="Users"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    surname=Column(String)
    username=Column(String,unique=True)
    email=Column(String,unique=True)  
    password=Column(String)
    hotel_rating=relationship("HotelRatingModel",back_populates="user")
    booking=relationship("BookingModel",back_populates="user")
    hotel=relationship("HotelModel",back_populates="user")

class HotelModel(Base):
    __tablename__="Hotels"
    id=Column(Integer,primary_key=True,index=True)
    hotel_name=Column(String)
    description=Column(String)
    adress=Column(String,unique=True)
    user_id=Column(Integer,ForeignKey("Users.id",ondelete="RESTRICT"),nullable=False)
    hotel_rating=relationship("HotelRatingModel",back_populates="hotel")
    room=relationship("RoomModel",back_populates="hotel")
    user=relationship("UserModel",back_populates="hotel")

class HotelRatingModel(Base):
    __tablename__="HotelRatings"
    id=Column(Integer,primary_key=True,index=True)
    rating=Column(Integer)
    review=Column(String)
    user_id=Column(Integer,ForeignKey("Users.id",ondelete="RESTRICT"),nullable=False)
    hotel_id=Column(Integer,ForeignKey("Hotels.id",ondelete="RESTRICT"),nullable=False)
    user=relationship("UserModel",back_populates="hotel_rating")
    hotel=relationship("HotelModel",back_populates="hotel_rating")

class BookingModel(Base):
    __tablename__="Bookings"
    id=Column(Integer,primary_key=True,index=True)
    checkin_date=Column(Date)
    checkout_date=Column(Date)
    booking_status=Column(Boolean)
    user_id=Column(Integer,ForeignKey("Users.id",ondelete="RESTRICT"),nullable=False)
    user=relationship("UserModel",back_populates="booking")
    booking_line=relationship("BookingLineModel",back_populates="booking")

class BookingLineModel(Base):
    __tablename__="BookingLinesModel"
    id=Column(Integer,primary_key=True,index=True)
    room_id=Column(Integer,ForeignKey("Rooms.id",ondelete="RESTRICT"),nullable=False)
    booking_id=Column(Integer,ForeignKey("Bookings.id",ondelete="RESTRICT"),nullable=False)
    booking=relationship("BookingModel",back_populates="booking_line")
    room=relationship("RoomModel",back_populates="booking_line")

class RoomModel(Base):
    __tablename__="Rooms"
    id=Column(Integer,primary_key=True,index=True)
    room_number=Column(Integer)
    size=Column(Integer)
    bed_count=Column(Integer)
    # bed_size=Column(Integer)
    price_per_night=Column(Integer)
    hotel_id=Column(Integer,ForeignKey("Hotels.id",ondelete="RESTRICT"),nullable=False)
    hotel=relationship("HotelModel",back_populates="room")
    booking_line=relationship("BookingLineModel",back_populates="room")
