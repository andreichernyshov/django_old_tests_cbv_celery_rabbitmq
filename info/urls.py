import debug_toolbar

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

app_name = 'info'

urlpatterns = [
    path('info/', ContactFormView.as_view(), name='info'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
