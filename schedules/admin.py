from django.contrib import admin
from . import models
from users import models as user_models

# Register your models here.
@admin.register(models.Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "pill",
        "date",
        "dosage",
    )