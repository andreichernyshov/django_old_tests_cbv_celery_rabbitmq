import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj_15.settings')
celery_app = Celery('proj_15')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
