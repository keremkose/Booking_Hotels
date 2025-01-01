from fastapi import Request,status
from app.exceptions.user_exceptions import UserNotFound
from fastapi.responses import JSONResponse,Response

def user_not_found_handler(request:Request,exc:UserNotFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail":exc.message}
    )
 