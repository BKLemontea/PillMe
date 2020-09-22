from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.
@admin.register(models.Pill)
class PillAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Pill Info",
            {
                "fields" : (
                    "date",
                    "image",
                    "name",
                    "serial_number",
                    "company_name",
                    "company_serial_number",
                    "sortation",
                    "nature",
                )
            },
        ),
        (
            "Feature Info",
            {
                "fields" : (
                    "mark_front",
                    "mark_back",
                    "shape",
                    "color_front",
                    "color_back",
                    "line_front",
                    "line_back",
                )
            },
        ),
        (
            "Size Info",
            {
                "fields" : (
                    "major_axis",
                    "minor_axis",
                    "thickness",
                )
            },
        ),
    )
    
    list_display = (
        "get_image",
        "name",
        "sortation",
        "mark_front",
        "mark_back",
        "shape",
        "color_front",
        "color_back",
        "company_name",
    )
    
    list_filter = (
        "sortation",
        "mark_front",
        "mark_back",
        "shape",
        "color_front",
        "color_back",
        "company_name",
    )
    
    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img width="100px" src="{obj.image.url}"/>')
        return "empty"
    get_image.short_description = "Image"