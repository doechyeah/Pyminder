import os, time
from celery import Celery

cel = Celery(__name__)

cel.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
cel.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")

@cel.task(name="create_task")
def create_task(task_type):
    time.sleep(int(task_type)*10)
    return True