from django.shortcuts import render

from .models import City
from .forms import ContactForm, CityForm, RegistrationForm, LoginForm
from celery import current_app
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, FormView, TemplateView
from django.contrib.auth.models import User, Group
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class CityDetailView(DetailView):
    model = City
    template_name = 'cbv/detail.html'


class AdminOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class StaffOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class CityCreateView(StaffOnlyMixin, CreateView):
    model = City
    template_name = 'cbv/create.html'
    success_url = '/'
    # fields = '__all__'
    # fields = ('name', 'kind', ...)
    # exclude = ('user',)
    form_class = CityForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)


class CityListView(ListView):
    model = City
    template_name = 'cbv/main.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['active_page'] = 'main'
        return context


class CityUpdateView(UpdateView):
    model = City
    template_name = 'cbv/update.html'
    success_url = '/'
    # fields = '__all__'
    form_class = CityForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)


class CityDeleteView(AdminOnlyMixin, DeleteView):
    model = City
    success_url = '/'
    template_name = 'cbv/delete.html'


# def index_view(request):
#     context = {}
#     animals = Animal.objects.select_related('kind', 'kind__family').all()
#     context['animals'] = animals
#     if request.method == 'POST':
#         result = send_mail_task.delay('scelery', 'stext')
#         context['task_id'] = result.id
#
#     context['active_page'] = '/'
#     return render(request, 'animals/index.html', context)


def status_view(request):
    task_id = request.GET['task_id']
    # По id получить задачу
    task = current_app.AsyncResult(task_id)
    status = task.status
    return render(request, 'cbv/status.html', {'status': status, 'task_id': task.id})


# Только для залогинентого
class ContactFormView(LoginRequiredMixin, FormView):
    template_name = 'cbv/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        text = form.cleaned_data['message']
        email = form.cleaned_data['email']
        send_mail_task.delay(subject, text, email)
        return super().form_valid(form)


class UserCreateView(CreateView):
    model = User
    form_class = RegistrationForm
    success_url = '/'
    template_name = 'cbv/register.html'


class LoginUserView(LoginView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'cbv/login.html'


class LogoutUserView(LogoutView):
    pass
