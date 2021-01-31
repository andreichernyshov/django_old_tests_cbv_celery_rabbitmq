from django.urls import path

from .views import CompanyProfileView

app_name = 'cbv'

urlpatterns = [
    path('create/', CompanyProfileView.as_view(), name='create.html'),
]
