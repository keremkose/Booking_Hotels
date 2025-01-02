from fastapi import FastAPI
from app.routers import booking_controller, hotel_controller, hotel_rating_controller, room_controller, user_controller, user_rating_controller
from app.models import models
from app.database import engine
from app.exceptions.user_exceptions import *
from app.services.exception_handler_service import user_not_found_handler
from fastapi.middleware.cors import CORSMiddleware
from app.auth import authentication_controller

app = FastAPI()

app.include_router(authentication_controller.router)
app.include_router(user_controller.router)
app.include_router(hotel_controller.router)
app.include_router(booking_controller.router)
app.include_router(hotel_rating_controller.router)
app.include_router(room_controller.router)
app.include_router(user_rating_controller.router)

#exception handlers
app.add_exception_handler(UserNotFound,user_not_found_handler)
#database
models.Base.metadata.create_all(engine)               
#cors
origins=[
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

