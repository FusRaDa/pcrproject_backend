from django.contrib import admin

# Register your models here.

from .models import Batch, Note
admin.site.register(Batch)
admin.site.register(Note)