from fastapi import APIRouter,Depends,Body,Header,Cookie,Form,Response,Request
from app.schemas.schemas import UserBase,UserDisplay
from app.services.database_service import get_db
from sqlalchemy.orm.session import Session
from app.database_services import user_database_service
from typing import Optional,List
from fastapi.responses import HTMLResponse
from app.services.oauth2_service import oauth2_scheme
from app.services.oauth2_service import get_current_user

router = APIRouter(prefix="/user", tags=["user"])


@router.post("")
def create_user(user: UserBase=Body(),db:Session=Depends(get_db)):
    user_database_service.create_user(user,db)

@router.get("")
def get_all_users(db:Session=Depends(get_db),user:UserDisplay=Depends(get_current_user)):
   return {
   "users":user_database_service.get_all_users(db),
   "user":user
   }

@router.get("/{id}")
def get_all_users(db:Session=Depends(get_db)):
   return user_database_service.get_user_by_userid(db)

@router.delete("/{id}")
def delete_user_by_id(id:int,db:Session=Depends(get_db)):
   return user_database_service.delete_user_by_id(id,db)


#TODO Delete below. PRACTICES
@router.get("/custom_response/{st}")
def custom_response(st:str):
   obj=f"""
      <head>
      <style>
      .objj{{
      width:50px;
      height:40px;
      background-color:green;   
      }}
      </style>
      </head>
      <div class="objj" >{st}</div>
      """ 
   return HTMLResponse(content=obj,media_type="text/html")

@router.get("/header")
def header_test(
   response:Response,
   custom_header:Optional[List[str]]=Header(None)
):
   response.headers["catched_header"]=",".join(custom_header)
   return 1

@router.get("/cookies/set/{cookievalue}")
def cookies(cookievalue: str = 'keko'):
   response=Response()
   response.set_cookie(key="test_cookie",value=cookievalue)
   return response 
   
@router.get("/cookies/get")
def cookies(test_cookie: Optional[str] = Cookie(None)):
   return {
      "test_cookie":test_cookie} 
   
@router.post("/form")
def form_func(form_data:str=Form(...)):
   return{
      "data":form_data
   }
