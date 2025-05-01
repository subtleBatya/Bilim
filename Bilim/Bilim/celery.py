from celery import Celery
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Bilim.settings")

app = Celery("Bilim")

app.config_from_object("Bilim.settings", namespace="CELERY")

app.autodiscover_tasks()


