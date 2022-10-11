from django.urls import path
from google_app.api import views

urlpatterns = [
    path("user/", views.ListView.as_view(), name="calender"),
    path("user/<int:pk>", views.DetailView.as_view(), name="detail"),
    path("lifeexpectancy/", views. ListViewLife.as_view(), name="life"),

]