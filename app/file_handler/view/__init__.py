from fastapi import APIRouter
from app.file_handler.view.view_file import router as router_file


router = APIRouter()

router.include_router(router_file)
