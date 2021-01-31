import time

from django.shortcuts import render
from django.views.generic import FormView
from .forms import ContactForm
from .models import Mesagesender
from .tasks import send_mail_task

from celery import current_app


class ContactFormView(FormView):
    template_name = 'mytasks/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        text = form.cleaned_data['message']
        email = form.cleaned_data['email']
        send_mail_task.delay(subject, text, email)
        return super().form_valid(form)
