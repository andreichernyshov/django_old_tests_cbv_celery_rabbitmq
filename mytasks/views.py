import time

from django.shortcuts import render

from .models import Mesagesender
from .tasks import send_mail_task


# from .tasks import index_view, send_mail_task

# from celery import current_app


def index_view(request):
    context = {}
    tasksen = Mesagesender.objects.select_related('tasksender', 'tasksender__family').all()
    context['mytasks'] = 'mytasks'
    if request.method == 'POST':
        result = send_mail_task.delay('scelery', 'text')
        context['result.id'] = result.id

    return render(request, 'reciever/index.html', context)










"""

def status_view(request):
    task_id = request.GET['task_id']
    task = current_app.AsyncResult(task_id)
    status = task.status
    return render(request, 'mytasks/status.html', {'status': status, 'task_id': task.id})


# context = {}

# context['mytasks'] = animals

# print(time.time())
# save_animal.delay()
# print(time.time())
# result = send_mail_task.delay('scelery', 'stext')
# context['task_id'] = result.id
# print(result.status)

# animals = Animal.objects.prefetch_related('foods').all()

# return render(request, 'animals/index.html', context)

# from django.core.mail import send_mail
# from django.shortcuts import render

# import time
# from celery import current_app

# def status_view(request):
# task_id = request.GET['task_id']
# По id получить задачу
# task = current_app.AsyncResult(task_id)
# status = task.status
# return render(request, 'animals/status.html', {'status': status, 'task_id': task.id})


"""
