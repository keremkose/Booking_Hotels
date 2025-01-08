from fastapi import FastAPI
from app.routers import booking_controller, hotel_controller, hotel_rating_controller, room_controller, user_controller, user_rating_controller,file_controller,booking_line_controller
from app.models import models
from app.services.database_service import engine
from app.exceptions.user_exceptions import *
from app.services.exception_handler_service import user_not_found_handler
from fastapi.middleware.cors import CORSMiddleware
from app.routers import authentication_controller
from fastapi.staticfiles import StaticFiles
from app.template import templates
# from app.middlewares.admin_addition_middleware import FirstUserAdminMiddleware

app = FastAPI()

#authentication
app.include_router(authentication_controller.router)
#file
app.include_router(file_controller.router)
#template
app.include_router (templates.router)
#db controllers
app.include_router(user_controller.router)
app.include_router(hotel_controller.router)
app.include_router(booking_controller.router)
app.include_router(booking_line_controller.router)
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
# app.add_middleware(FirstUserAdminMiddleware)

app.mount("/files",StaticFiles(directory="app/static_files"),name="files")
app.mount("/template",StaticFiles(directory="app/template"),name="styleget")

def get_app():
    return app