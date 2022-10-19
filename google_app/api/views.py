from rest_framework import generics
from google_app.models import Accounts,LifeExpectancy
from google_app.api.serializers import AccountsSerializer,LifeSeializer

class ListView(generics.ListCreateAPIView):
    queryset = Accounts.objects.all().order_by('-id')
    serializer_class = AccountsSerializer

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer

class ListViewLife(generics.ListCreateAPIView):
    queryset =  LifeExpectancy.objects.all()
    serializer_class = LifeSeializer