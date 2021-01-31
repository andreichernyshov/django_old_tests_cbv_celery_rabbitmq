from django.urls import path

from .views import ContactFormView

app_name = 'mytasks'


urlpatterns = [
    path('contact/', ContactFormView.as_view(), name='contact.html'),
]


# path('status/', status_view, name='status'),
