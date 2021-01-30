import time

from celery import shared_task
from .models import Mesagesender


@shared_task
def send_mail_task(subject, text):
    mytasks = (subject, text, 'zimacool@zimacool.com', ['zimacool@zimacool.com', 'admin@admin.com'], 'fail_silently=False')
