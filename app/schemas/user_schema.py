from pydantic import BaseModel

class UserSchema(BaseModel):
    name:str
    surname:str
    username:str
    email:str
    password:str

class UserDTO(BaseModel): 
    name:str
    surname:str
    username:str
    email:str
    class Congif():
        from_attribute=True