from fastapi import FastAPI
from app.routers import booking_controller, hotel_controller, hotel_rating_controller, room_controller, user_controller, user_rating_controller


app = FastAPI()

app.include_router(booking_controller)
app.include_router(user_controller)
app.include_router(hotel_controller)
app.include_router(hotel_rating_controller)
app.include_router(room_controller)
app.include_router(user_rating_controller)
