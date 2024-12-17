from passlib.context import CryptContext

password_context=CryptContext(schemes='bcrypt',deprecated='auto')

class Hash():
    def bcrypt(password:str):
        return password_context.hash(password)
    def verify(hashed_password:str,password:str):
        return password_context.verify(password,hashed_password)