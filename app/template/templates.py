from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import  HTMLResponse
from fastapi.requests import Request
 

router=APIRouter(prefix="/templates",tags=["templates"])
templates = Jinja2Templates(directory="app/template")

@router.get("/hotels/{id}",response_class=HTMLResponse)

def template(id:int,req:Request):
    return templates.TemplateResponse(
        "hotel.html",
        {
            "request":req,
            "id":id
        })