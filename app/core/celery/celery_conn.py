from celery import Celery
from app.core.config import settings

celery = Celery('hello', backend=settings.REDIS_ENDPOINT, broker=settings.REDIS_ENDPOINT)

celery.backend.cleanup()
# Disable task result save in redis
celery.conf.task_ignore_result = True
celery.conf.task_store_errors_even_if_ignored = True
celery.conf.timezone = 'UTC'