from django.contrib import admin

# Register your models here.

from .models import Assay, Batch, Note
admin.site.register(Batch)
admin.site.register(Note)
admin.site.register(Assay)
