from django.contrib import admin

# Register your models here.

from .models import Assay, Batch, Label, Reagent, Supply
admin.site.register(Batch)
admin.site.register(Assay)
admin.site.register(Reagent)
admin.site.register(Supply)
admin.site.register(Label)

