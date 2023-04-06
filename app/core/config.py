from typing import Optional, List, Union, Tuple
from pydantic import BaseSettings
import os


class AppEnvConfig(BaseSettings):
    
    APP_PROJECT_NAME: str = "FastApi-App"
    APP_DEBUG: bool = True
    APP_DOCS_URL: Optional[str] = '/docs'

    GUNICORN_HOST: str = '0.0.0.0'
    GUNICORN_PORT: str = '3000'
    
    APP_DB_MONGO_URI : str = ''
    APP_DB_MONGO_NAME : str = ''
    
    MINIO_ENDPOINT : str = ''
    MINIO_ACCESS_KEY : str = ''
    MINIO_SECRET_KEY : str = ''
    MINIO_SECURE : bool = False
    MINIO_LIST_BUCKET : list = ['excel','images','video','mp3']  

    SECRET_KEY : str =  ''
    SECURITY_ALGORITHM : str = 'HS256'
     
    class Config:
        case_sensitive = True
        validate_assignment = True
        
        
    

settings = AppEnvConfig(_env_file='.env')
if __name__ == "__main__":
    pass



        
    