from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    GENDER_MALE = "남"
    GENDER_FEMALE = "여"

    GENDER_CHOICES = (
        (GENDER_MALE, "남"),
        (GENDER_FEMALE, "여"),
    )
    
    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    
    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
    )
    
    name = models.CharField(max_length=10)
    birthdate = models.DateField(blank = True, null = True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    address = models.CharField(max_length=100, blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    email_service = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)
    login_method = models.CharField(choices=LOGIN_CHOICES, max_length=10, default=LOGIN_EMAIL)
    
    def __str__(self):
        return self.name