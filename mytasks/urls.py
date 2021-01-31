from django.urls import path

from .views import ContactFormView, StatusFormView

app_name = 'mytasks'


urlpatterns = [
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('status/', StatusFormView.as_view(), name='status'),
]
