import logging
from minio import Minio
from minio.error import S3Error
from app.core.config import settings
from app.core.abstractions import Singleton

logger = logging.getLogger("Minio")

minio_client = Minio(
    endpoint= settings.MINIO_ENDPOINT,
    access_key= settings.MINIO_ACCESS_KEY,
    secret_key= settings.MINIO_SECRET_KEY,
    secure= settings.MINIO_SECURE
)

class MinioClient(metaclass=Singleton):
    def __init__(self) -> None:
        self.endpoint = settings.MINIO_ENDPOINT
        self.access_key = settings.MINIO_ACCESS_KEY
        self.secret_key = settings.MINIO_SECRET_KEY
        self.secure = settings.MINIO_SECURE
        self.list_buckets = settings.MINIO_LIST_BUCKET
        
        try:
            self.client = Minio(
                endpoint = self.endpoint,
                access_key = self.access_key,
                secret_key = self.secret_key,
                secure = self.secure
            )
        except S3Error as e:
            logger.error(f"Try to connect MinIO get exception {e.message}")
    
    def generate_buckets(self):
        for bucket in self.list_buckets:
            found_bucket = self.client.bucket_exists(bucket)
            if not found_bucket:
                self.client.make_bucket(bucket)
                print(f"Created new bucket - {bucket}")
    
    def check_file_exist(self, name_bucket, name_object):
        try:
            list_object = self.client.list_objects(name_bucket)
            if name_object not in [_object.object_name for _object in list_object]:
                logger.critical(f"File {name_object} not exist in bucket {name_bucket}")
                return None
            return True
        except S3Error as e:
            logger.critical(f"Get file in Minio not success - {e.message}")
            return None
        
    
    def get_url_object(self,name_bucket: str, name_object: str):
        try: 
            check = self.check_file_exist(name_bucket, name_object)
            if check:
                url_object = self.client.presigned_get_object(bucket_name= name_bucket,
                                                            object_name= name_object)
                return url_object
            else:
                return None
        except S3Error as e:
            print(f'Cant get url object from minio got error {e._message}')
            return None

    

minio_client = MinioClient()
    