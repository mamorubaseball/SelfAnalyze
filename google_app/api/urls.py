from django.urls import path
from google_app.api import views

urlpatterns = [
    path("googleCalender/", views.ListView.as_view(), name="calender"),
    path("googleCalender/<int:pk>", views.DetailView.as_view(), name="detail"),
]