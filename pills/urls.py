from django.urls import path
from . import views

app_name = "pills"

urlpatterns = [
    path("<int:pk>/detail/", views.PillDetailView.as_view(), name="detail"),
    path("camera/", views.camera, name="camera"),
    path("search/", views.search, name="search"),
]