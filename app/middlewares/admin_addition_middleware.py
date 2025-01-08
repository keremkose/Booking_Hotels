# from fastapi import FastAPI, HTTPException, Request,Depends
# from starlette.middleware.base import BaseHTTPMiddleware
# from sqlalchemy.orm import Session
# from app.services.database_service import SessionLocal
# from app.models.models import UserModel
# import os
# from app.config import settings
# from app.services.database_service import get_db

# class FirstUserAdminMiddleware(BaseHTTPMiddleware):
#     def __init__(self, app: FastAPI,db:=Depends(get_db)):
#         super().__init__(app)
#         self.db = db  

#     async def dispatch(self, request: Request, call_next):
#         if settings.admin_is_there is False:
           
          
#             user=UserModel(
#                 name=settings.admin_name,
#                 surname=settings.admin_surname,
#                 username=settings.admin_username,
#                 password=settings.admin_password                    
                    
#             )
#             self.db.add(user)
#             self.db.commit()
#             settings.admin_is_there=True
#         response = await call_next(request)
#         return response
    
    
    
# # from fastapi import FastAPI, HTTPException, Request
# # from starlette.middleware.base import BaseHTTPMiddleware
# # from sqlalchemy.orm import Session
# # from app.services.database_service import SessionLocal
# # from app.models.models import UserModel
# # import os

# # class FirstUserAdminMiddleware(BaseHTTPMiddleware):
# #     def __init__(self, app: FastAPI):
# #         super().__init__(app)
# #         self._admin_assigned = False  # Flag to ensure admin is assigned only once

# #     async def dispatch(self, request: Request, call_next):
# #         if not self._admin_assigned:
# #             # Create a new database session
# #             db: Session = SessionLocal()

# #             try:
# #                 # Check if there are any admins in the database
# #                 admin_count = db.query(UserModel).filter(UserModel.is_admin == True).count()

# #                 if admin_count == 0:
# #                     # If no admin exists, make the first user as admin
# #                     first_user = db.query(UserModel).first()
# #                     if first_user:
# #                         first_user.is_admin = True
# #                         db.commit()
# #                         db.refresh(first_user)

# #                     self._admin_assigned = True  # Set the flag to true to avoid further DB requests
# #                 else:
# #                     self._admin_assigned = True  # Mark as done even if an admin exists

# #             except Exception as e:
# #                 db.rollback()
# #                 raise HTTPException(status_code=500, detail="Internal Server Error while assigning admin.")
# #             finally:
# #                 db.close()

# #         # Proceed with the rest of the request pipeline
# #         response = await call_next(request)
# #         return response