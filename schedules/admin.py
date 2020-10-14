from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "pill",
        "user",
    )
    
@admin.register(models.DayOfWeek)
class DayOfWeekAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )