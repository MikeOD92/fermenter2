from django.contrib import admin
from .models import Recipe, Batch
# Register your models here.

admin.site.register(Recipe)
admin.site.register(Batch)