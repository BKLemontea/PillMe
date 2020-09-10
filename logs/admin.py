from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Log)
class LogAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "dosage",
        "created",
        "user",
    )
    
    list_filter = (
        "name",
        "user",
    )