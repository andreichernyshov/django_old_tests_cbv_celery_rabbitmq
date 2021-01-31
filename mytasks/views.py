import time

from django.shortcuts import render
from django.views.generic import FormView
from .forms import ContactForm, StatusForm

from .tasks import send_mail_task

from celery import current_app


class StatusFormView(FormView):
    template_name = 'mytasks/status.html'


class ContactFormView(FormView):
    template_name = 'mytasks/contact.html'
    form_class = ContactForm
    success_url = StatusForm()

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        when_to_do = form.cleaned_data['when_to_do']
        email = form.cleaned_data['email']
        send_mail_task.delay(subject, when_to_do, email)
        return super().form_valid(form)
