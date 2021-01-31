from django.shortcuts import render

from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.views.generic import FormView, TemplateView

from .models import CompanyProfile


class CompanyProfileView(CreateView):
    model = CompanyProfile
    template_name = 'cbv/create.html'







"""
def home_view(request):
    qr_st = Vacancy.objects.all()
    return render(request, 'parsing/home.html', {'object_list': qr_st})
"""
