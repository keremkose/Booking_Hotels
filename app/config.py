from pydantic_settings import BaseSettings
from dotenv import load_dotenv

#TODO loads both environments. needs to be adjusted.
#TODO put ENV varaibles in .env
load_dotenv(dotenv_path=".env") 
load_dotenv(dotenv_path=".env.secret")  

class Settings(BaseSettings):

    app_name: str
    app_version: str
    debug: bool
    database_url: str
    logging_path:str

    secret_key: str
    database_password: str
    api_key: str
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

print(settings.app_name)
print(settings.app_version)


