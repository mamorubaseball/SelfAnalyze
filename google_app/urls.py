from django.urls import path
from . import views
from google_app.views import IndexView,Login,AccountRegistration,home,Logout


app_name = 'google_app'
urlpatterns = [
    # path('',IndexView.as_view(),name='index'),
    path('',Login,name = 'Login'),
    path('logout',Logout,name = 'Logout'),
    path('register',AccountRegistration.as_view(),name = 'register'),
    path('home',home,name= "home")
    ]