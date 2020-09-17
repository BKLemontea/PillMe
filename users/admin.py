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
                    "login_method",
                )
            },
        ),
        (
            "Services",
            {
                "fields" : (
                    "email_service",
                )
            },
        ),
        (
            "Inventory",
            {
                "fields" : (
                    "inventory",
                )
            },
        ),
        (
            "Email Login",
            {
                "fields" : (
                    "email_verified",
                    "email_secret",
                )
            },
        ),
    )
    
    list_display = (
        "email",
        "name",
        "birthdate",
        "gender",
        "login_method",
    )
    
    filter_horizontal = (
        "inventory",
    )