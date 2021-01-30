import debug_toolbar

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mytasks.urls', namespace='mytasks')),
    path('__debug__/', include(debug_toolbar.urls)),
]

# from django.conf import settings
