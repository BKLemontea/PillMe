from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("<int:pk>/add/", views.add_inventory, name="add"),
    path("<int:pk>/delete/", views.delete_inventory, name="delete"),
]
