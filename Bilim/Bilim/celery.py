from celery import Celery
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Bilim.settings")

app = Celery("Bilim")

app.config_from_object({
    'broker_url': 'redis://localhost:6380/0',
    'result_backend': 'redis://localhost:6380/0',
    'accept_content': ['json'],
    'task_serializer': 'json',
    'result_serializer': 'json',
    'timezone': 'Asia/Ashgabat',
})

app.autodiscover_tasks()


