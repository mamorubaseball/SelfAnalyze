from django.urls import path
from . import views
from google_app.views import IndexView


app_name = 'google_app'
urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    ]