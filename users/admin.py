from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields" : (
                    "name",
                    "birthdate",
                    "gender",
                    "address",
                    "email_verified",
                    "email_service",
                    "email_secret",
                    "login_method",
                )
            }
        ),
    )
    
    list_display = (
        "name",
        "birthdate",
        "gender",
        "login_method",
    )