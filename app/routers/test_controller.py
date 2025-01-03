##TODO Delete file
from fastapi.routing import APIRouter
from fastapi import FastAPI,Request,Body
from sys import getsizeof
from app.services.logging_service import log

router=APIRouter(prefix="/test", tags=["test"])


@router.post("")
async def test_route(req:Request):
    log("test","test log for test")
    data= await req.body()
    print(data)
    pass

@router.get("")
async def test_route():
    log("get","test log for test")
    pass