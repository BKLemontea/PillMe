from django.urls import path
from . import views

app_name = "pills"

urlpatterns = [
    path("<int:pk>/detail/", views.PillDetailView.as_view(), name="detail"),
    path("camera/", views.camera, name="camera"),
    path("<int:pk>/add/", views.add_inventory, name="add"),
    path("<int:pk>/delete/", views.delete_inventory, name="delete"),
]