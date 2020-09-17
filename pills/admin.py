from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.
@admin.register(models.Pill)
class PillAdmin(admin.ModelAdmin):
    list_display = (
        "get_thumnnail",
        "name",
        "cycle",
        "dosage",
    )
    
    list_filter = (
        "name",
    )
    
    def get_thumnnail(self, obj):
        return mark_safe(f'<img width="100px" src="{obj.file.url}"/>')
    get_thumnnail.short_description = "Thumnnail"