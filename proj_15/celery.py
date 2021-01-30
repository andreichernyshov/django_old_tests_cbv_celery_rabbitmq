import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj_15.settings')

app = Celery('proj_15')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
