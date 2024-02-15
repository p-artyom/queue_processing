import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'creating_queue.settings')
app = Celery('creating_queue')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
