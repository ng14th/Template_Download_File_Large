from pydantic import BaseModel, validator
from typing import Optional
from app.core.schema.exception import ErrorResponseException
from app.core.schema.api_respone import get_error_code

class NameFileInput(BaseModel):
    name : str
    type : str
    
    @validator('type')
    def _validator_type(cls,v):
        if v not in ['excel', 'images', 'mp3', 'video']:
            raise ErrorResponseException(**get_error_code(1001))
        return v