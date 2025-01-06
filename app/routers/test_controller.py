##TODO Delete file
from fastapi.routing import APIRouter
from fastapi import FastAPI,Request,Body
from sys import getsizeof
from app.services.logging_service import log
import asyncio
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.requests import Request,HTTPConnection
router=APIRouter(prefix="/test", tags=["test"])

def asd():
    print("asd worked")

@router.post("")
async def test_route(req:Request):
    await asyncio.sleep(10)
    print("post worked")
    pass

@router.get("")
def test_route():
 
        print("get worked")

    # print(req.url)
    # print(req.app)
    # print(req.base_url)
    # print(req.client)
    # print(req.cookies)
    # print(req.headers)
    # print(req.body())
    # print(req.method)
   
    