from app.core.database.minio import minio_client
from app.file_handler.schema.schema import NameFileInput
from app.core.schema.exception import ErrorResponseException
from app.core.schema.api_respone import get_error_code


async def get_url_from_minio(data: NameFileInput):
    file_name = data.name
    folder_type = data.type

    if folder_type == 'excel':
        file_name = f'{data.name}.xlsx'

    elif folder_type == 'mp3':
        file_name = f'{data.name}.mp3'

    elif folder_type == 'video':
        file_name = f'{data.name}.mp4'

    elif folder_type == 'images':
        file_name = f'{data.name}.jpg'

    url_file = minio_client.get_url_object(folder_type, file_name)
    if url_file:
        return url_file
    else:
        raise ErrorResponseException(**get_error_code(1003))
