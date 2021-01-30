from celery import shared_task
import time
from .models import Mesagesender


@shared_task
def send_mail_task(subject, text):
    send_mail = (subject, text, 'zimacool@zimacool.com', ['zimacool@zimacool.com', 'admin@admin.com'], 'fail_silently=False')
