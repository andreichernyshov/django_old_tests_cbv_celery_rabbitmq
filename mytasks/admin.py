from django.contrib import admin

from .models import Mesagesender
from .models import Tasksender

admin.site.register(Mesagesender)
admin.site.register(Tasksender)
