#TODO delete the file

from json.decoder import JSONDecoder  
from json.encoder import JSONEncoder
from fastapi.requests import Request
import os

## JSON encode
# a :str= " { 'Kerem':'Kose'}  "
# enc= JSONEncoder()
# print(enc.encode(a))


#
# req= Request()
# req.base_url="http://baseurl"
# new_url=req.url_for("kerem")
# print(new_url)

#
# os.abort()
# print()

## Class creation 
# class A():
#     ad:str
#     soyad:str
    
#     def __init__(self, ad:str, soyad:str):
#         self.ad=ad
#         self.soyad=soyad

# aa= A("kerem","kose")
# aa.ad="buark"
# aa.soyad="kose"
# print(aa.ad)




# #TODO Delete below. PRACTICES
# @router.get("/custom_response/{st}")
# def custom_response(st:str):
#    obj=f"""
#       <head>
#       <style>
#       .objj{{
#       width:50px;
#       height:40px;
#       background-color:green;   
#       }}
#       </style>
#       </head>
#       <div class="objj" >{st}</div>
#       """ 
#    return HTMLResponse(content=obj,media_type="text/html")

# @router.get("/header")
# def header_test(
#    response:Response,
#    custom_header:Optional[List[str]]=Header(None)
# ):
#    response.headers["catched_header"]=",".join(custom_header)
#    return 1

# @router.get("/cookies/set/{cookievalue}")
# def cookies(cookievalue: str = 'keko'):
#    response=Response()
#    response.set_cookie(key="test_cookie",value=cookievalue)
#    return response 
   
# @router.get("/cookies/get")
# def cookies(test_cookie: Optional[str] = Cookie(None)):
#    return {
#       "test_cookie":test_cookie} 
   
# @router.post("/form")
# def form_func(form_data:str=Form(...)):
#    return{
#       "data":form_data
#    }
