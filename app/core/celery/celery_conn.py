from celery import Celery
from app.core.config import settings

celery = Celery('hello', backend='rpc://', broker="amqp://admin:admin@172.27.230.14:5672/nguyennt63")

celery.backend.cleanup()
# Disable task result save in redis
celery.conf.task_ignore_result = True
celery.conf.task_store_errors_even_if_ignored = True
celery.conf.timezone = 'UTC'