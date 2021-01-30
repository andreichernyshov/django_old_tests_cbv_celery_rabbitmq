from django.urls import path

from .views import index_view

app_name = 'mytasks'


urlpatterns = [
    path('', index_view, 'mytasks/index.html'),
]


# path('status/', status_view, name='status'),
