from pydantic import BaseModel, validator
from typing import Optional
from app.core.schema.exception import ErrorResponseException
from app.core.schema.api_respone import get_error_code

class NameFileInput(BaseModel):
    filename : str 