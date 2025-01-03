from fastapi import APIRouter,File,UploadFile
import shutil
from fastapi.responses import FileResponse

router=APIRouter(prefix="/file",tags=["file"])

@router.post("/bytes")
def get_file(file:bytes=File(...)):
    content= file.decode("utf-8")
    lines=content.split("\n")
    return{"lines":lines}

@router.post("/upload_file")
def get_upload_file(upload_file:UploadFile=File(...)):  
    
    path= f"app/routers/test_storage/{upload_file.filename}"
    
    with open(path, "w+b") as buffer: 
        shutil.copyfileobj(upload_file.file,buffer)
    
    return{"file_name": path ,
           "type":upload_file.content_type
           }
    
@router.get("/download/{file_name}",response_class=FileResponse)
def get_file(file_name:str):
    path=f"app/static_files/{file_name}"
    return path