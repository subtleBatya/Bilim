redis-server --port 6380
celery -A Bilim worker --loglevel=INFO --pool=prefork
celery -A Bilim beat --scheduler django_celery_beat.schedulers:DatabaseScheduler --loglevel=INFO
