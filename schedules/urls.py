from django.urls import path
from . import views

app_name = "schedules"

urlpatterns = [
    path("/", views.schedule_list, name="list"),
    path("<int:pk>/add/", views.AddScheduleView.as_view(), name="add"),
    path("<int:pk>/add-f/", views.add_schedule, name="add-f"),
]