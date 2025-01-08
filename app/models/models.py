from sqlalchemy import  Column,ForeignKey,Table,CheckConstraint
from app.services.database_service import Base,engine
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import String,Integer,Boolean,Date
from sqlalchemy.orm import validates
import re

max_credential_length=15
max_text_length=100

class UserModel(Base):
    __tablename__="Users"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(max_credential_length))
    surname=Column(String(max_credential_length))
    username=Column(String(max_credential_length),unique=True)
    email=Column(String,unique=True) 
    password=Column(String)
    is_admin=Column(Boolean(False))
    
    hotel_rating=relationship("HotelRatingModel",back_populates="user")
    booking=relationship("BookingModel",back_populates="user")
    hotel=relationship("HotelModel",back_populates="user")
    user_rating=relationship("UserRatingModel",back_populates="user")
    
    @validates('name')
    def validate_comment(self, key, value):
        if len(value) > max_credential_length:
            raise ValueError(f"Name cannot exceed {max_text_length} characters. Provided comment length: {len(value)}")
        return value  
    @validates('surname')
    def validate_comment(self, key, value):
        if len(value) > max_credential_length:
            raise ValueError(f"Surname cannot exceed {max_text_length} characters. Provided comment length: {len(value)}")
        return value  
    @validates('username')
    def validate_comment(self, key, value):
        if len(value) > max_credential_length:
            raise ValueError(f"Username cannot exceed {max_text_length} characters. Provided comment length: {len(value)}")
        return value
    
    @validates("email")
    def validate_email(self, key, email):
        """Validate email format."""
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.match(email_regex, email):
            raise ValueError(f"Invalid email address: {email}")
        return email
    

class HotelModel(Base):
    __tablename__="Hotels"
    id=Column(Integer,primary_key=True,index=True)
    hotel_name=Column(String(max_credential_length),unique=True)
    description=Column(String(max_text_length))
    adress=Column(String(max_text_length))
    user_id=Column(Integer,ForeignKey("Users.id"),nullable=False)
    
    hotel_rating=relationship("HotelRatingModel",back_populates="hotel")
    room=relationship("RoomModel",back_populates="hotel")
    user=relationship("UserModel",back_populates="hotel")
    user_rating=relationship("UserRatingModel",back_populates="hotel")
    
    @validates('hotel_name')
    def validate_comment(self, key, value):
        if len(value) > max_credential_length:
            raise ValueError(f"Hotel name cannot exceed {max_text_length} characters. Provided comment length: {len(value)}")
        return value  
    @validates('description')
    def validate_comment(self, key, value):
        if len(value) > max_text_length:
            raise ValueError(f"Description cannot exceed {max_text_length} characters. Provided comment length: {len(value)}")
        return value  
    @validates('adress')
    def validate_comment(self, key, value):
        if len(value) > max_text_length:
            raise ValueError(f"Adress cannot exceed {max_text_length} characters. Provided comment length: {len(value)}")
        return value

class HotelRatingModel(Base):
    __tablename__="HotelRatings"
    id=Column(Integer,primary_key=True,index=True)
    rate=Column(Integer)
    review=Column(String(max_text_length))
    user_id=Column(Integer,ForeignKey("Users.id"),nullable=False)
    hotel_id=Column(Integer,ForeignKey("Hotels.id"),nullable=False)
    
    user=relationship("UserModel",back_populates="hotel_rating")
    hotel=relationship("HotelModel",back_populates="hotel_rating")
    
      
    @validates('rate')
    def validate_rate(self, key, value):
        if value < 1 or value > 10:
            raise ValueError("Rate must be an integer between 1 and 10.")
        return value

    @validates('review')
    def validate_comment(self, key, value):
        if len(value) > max_text_length:
            raise ValueError(f"Review cannot exceed {max_text_length} characters. Provided comment length: {len(value)}")
        return value

class BookingModel(Base):
    __tablename__="Bookings"
    id=Column(Integer,primary_key=True,index=True)
    checkin_date=Column(Date)
    checkout_date=Column(Date)
    booking_status=Column(Boolean)
    user_id=Column(Integer,ForeignKey("Users.id"),nullable=False)
    
    user=relationship("UserModel",back_populates="booking")
    booking_line=relationship("BookingLineModel",back_populates="booking")

class BookingLineModel(Base):
    __tablename__="BookingLinesModel"
    id=Column(Integer,primary_key=True,index=True)
    room_id=Column(Integer,ForeignKey("Rooms.id"),nullable=False)
    booking_id=Column(Integer,ForeignKey("Bookings.id"),nullable=False)
    
    booking=relationship("BookingModel",back_populates="booking_line")
    room=relationship("RoomModel",back_populates="booking_line")

class RoomModel(Base):
    __tablename__="Rooms"
    id=Column(Integer,primary_key=True,index=True)
    room_number=Column(Integer,unique=True)
    size=Column(Integer)
    bed_count=Column(Integer)
    price_per_night=Column(Integer)
    hotel_id=Column(Integer,ForeignKey("Hotels.id"),nullable=False)
    
    hotel=relationship("HotelModel",back_populates="room")
    booking_line=relationship("BookingLineModel",back_populates="room")

class UserRatingModel(Base):
    __tablename__="UserRatings"
    id=Column(Integer,primary_key=True,index=True)
    manager_user_id=Column(Integer,ForeignKey("Hotels.id"),nullable=False)
    customer_user_id=Column(Integer,ForeignKey("Users.id"),nullable=False)
    rate=Column(Integer,CheckConstraint('rate BETWEEN 1 AND 5'),) #TODO Adjust it to Enum or ...
    comment=Column(String(max_text_length)) 
    
    hotel=relationship("HotelModel",back_populates="user_rating")
    user=relationship("UserModel",back_populates="user_rating")
    
    @validates('rate')
    def validate_rate(self, key, value):
        if value < 1 or value > 10:
            raise ValueError("Rate must be an integer between 1 and 10.")
        return value

    @validates('comment')
    def validate_comment(self, key, value):
        if len(value) > max_text_length:
            raise ValueError(f"Comment cannot exceed {max_text_length} characters. Provided comment length: {len(value)}")
        return value