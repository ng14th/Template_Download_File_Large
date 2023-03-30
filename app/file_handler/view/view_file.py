from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse, FileResponse
from app.core.schema.api_respone import ApiResponse
from ..schema.schema import NameFileInput

router = APIRouter(tags=['File Handler'])

@router.post('/request_download_file', response_model=ApiResponse)
async def request_download_file(
    data : NameFileInput
):
    pass
    return
@router.post('/download_file')
async def download_file(
    data : NameFileInput
):
    pass
    return

@router.get('/test_download_file')
async def test_download_file():
    pass
    return
    