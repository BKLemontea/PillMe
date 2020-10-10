from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.log_out, name="logout"),
    path("<int:pk>/add/", views.add_inventory, name="add"),
    path("<int:pk>/delete/", views.delete_inventory, name="delete"),
    path("inventroy/", views.InventoryView.as_view(), name="inventory")
]
