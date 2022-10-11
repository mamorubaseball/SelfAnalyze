from rest_framework import generics
from google_app.models import User,LifeExpectancy
from google_app.api.serializers import UserSerializer,LifeSeializer

class ListView(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListViewLife(generics.ListCreateAPIView):
    queryset =  LifeExpectancy.objects.all()
    serializer_class = LifeSeializer