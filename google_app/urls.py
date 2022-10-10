# from importlib.resources import path
from django.urls import re_path
from django.conf.urls import url
from django.urls import path
from . import views
from google_app.views import IndexView

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    ]