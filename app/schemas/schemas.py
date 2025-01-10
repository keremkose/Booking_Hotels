from pydantic import BaseModel
from datetime import date

#User Schemas

#Update
class UserUpdateBase(BaseModel):
    name:str|None
    surname:str|None
    username:str|None
    password:str|None
    email:str|None

class UserBase(BaseModel):
    name:str
    surname:str
    username:str
    email:str
    password:str

class UserDisplay(BaseModel): 
    id:int
    name:str
    surname:str
    username:str
    email:str
    class Congif():
        from_attribute=True

#Hotel Schemas
class HotelBase(BaseModel):
    hotel_name:str
    description:str
    adress:str

class HotelUpdateBase(BaseModel):
    id:int
    hotel_name:str|None
    description:str|None
    adress:str|None
    
class HotelDisplay(BaseModel): 
    id:int
    hotel_name:str
    description:str
    adress:str
    class Congif():
        from_attribute=True

#HotelRating Schemas
class HotelRatingBase(BaseModel):
    rate:int
    review:str
    hotel_id:int

class HotelRatingUpdateBase(BaseModel):
    id:int
    rate:int|None
    review:str|None
    user_id:int|None
    hotel_id:int|None

class HotelRatingDisplay(BaseModel): 
    id:int
    rate:int
    review:str
    hotel_id:int
    class Congif():
        from_attribute=True

#Booking Schemas
class BookingBase(BaseModel):
    checkin_date:date           #ask to jurgen
    checkout_date:date

class BookingUpdateBase(BaseModel):
    checkin_date:date|None           #ask to jurgen
    checkout_date:date|None
    booking_status:bool|None
    id:int

class BookingDisplay(BaseModel): #ask to jurgen
    id:int
    checkin_date:date
    checkout_date:date
    booking_status:bool
    user_id:int #TODO
    class Congif():
        from_attribute=True

#BookingLine Schemas
class BookingLineBase(BaseModel):
    booking_id:int
    room_id:int

class BookingLineUpdateBase(BaseModel):
    id:int
    booking_id:int|None
    room_id:int|None

class BookingLineDisplay(BaseModel): 
    id:int
    booking_id:int
    room_id:int
    class Congif():
        from_attribute=True
       
#Room Schemas
class RoomBase(BaseModel):
    room_number:int
    size:int
    bed_count:int
    price_per_night:int
    hotel_id:int

class RoomUpdateBase(BaseModel):
    id:int
    room_number:int |None
    size:int|None
    bed_count:int|None
    price_per_night:int|None
    hotel_id:int

class RoomDisplay(BaseModel): 
    id:int
    room_number:int
    size:int
    bed_count:int
    price_per_night:int
    hotel_id:int
    class Congif():
        from_attribute=True

#UserRating Schemas

class UserRatingBase(BaseModel):
    manager_user_id:int
    customer_user_id :int
    rate:str
    comment:str

class UserRatingUpdateBase(BaseModel):
    id:int
    manager_user_id:int
    customer_user_id :int
    rate:str
    comment:str

class UserRatingDisplay(BaseModel):
    id:int
    manager_user_id:int
    customer_user_id :int
    rate:str
    comment:str
    class Congif():
        from_attribute=True
