from django.urls import path
from . import views
from google_app.views import IndexView

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    ]