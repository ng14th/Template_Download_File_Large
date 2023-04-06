import logging
from fastapi import FastAPI, Request, BackgroundTasks
from app.core.config import settings
from app.file_handler.view import router as router_file
from fastapi.responses import JSONResponse, HTMLResponse
from app.core.schema.exception import ErrorResponseException
from fastapi.middleware.cors import CORSMiddleware
from app.core.database.minio import minio_client
from app.core.startup_event.crontask import events



log = logging.getLogger(__name__)

app = FastAPI(
    title=settings.APP_PROJECT_NAME,
    docs_url= settings.APP_DOCS_URL,
    openapi_url='/api/openapi.json',
    on_startup= events
)

app.add_middleware(CORSMiddleware,
                   allow_origins=["http://localhost:800*","*"],
                   allow_methods = ["POST", "GET", "DELETE", "PUT"],
                   allow_credentials = True,
                   allow_headers = ["*"])

for router in (
    {'module': router_file, 'prefix': '/file',},
):
    app.include_router(
        router.get('module'),
        prefix=router.get('prefix'),
        tags = router.get('tags')
    )


@app.exception_handler(ErrorResponseException)
async def error_response_exception_handler(request: Request, exception: ErrorResponseException):
    return JSONResponse(
        status_code=exception.status_code,
        content={
            "success": exception.success,
            "data": exception.data,
            "length": exception.length,
            "error": exception.error,
            "error_code": exception.error_code
        },
    )
    
minio_client.generate_buckets()

@app.get("/")
async def root():    
    
    return {"message": "Hello World"}


    