from fastapi import FastAPI
from app.routers import booking_controller, hotel_controller, hotel_rating_controller, room_controller, user_controller, user_rating_controller
from app.models import models
from app.database import engine

app = FastAPI()

app.include_router(user_controller.router)
app.include_router(hotel_controller.router)
# app.include_router(booking_controller)
# app.include_router(hotel_rating_controller)
# app.include_router(room_controller)
# app.include_router(user_rating_controller)

models.Base.metadata.create_all(engine)