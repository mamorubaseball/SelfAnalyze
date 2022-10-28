from rest_framework import generics
from google_app.models import Accounts,LifeExpectancy
from google_app.api.serializers import AccountsSerializer,LifeSeializer

class ListView(generics.ListCreateAPIView):
    queryset = Accounts.objects.all().order_by('-id')
    serializer_class = AccountsSerializer
    filter_fields = ('user',)  #追加
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Accounts.objects.all()
        userid = self.request.query_params.get('user')
        if userid is not None:
            queryset = queryset.filter(user=userid)
        return queryset
    
class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer

class ListViewLife(generics.ListCreateAPIView):
    queryset =  LifeExpectancy.objects.all()
    serializer_class = LifeSeializer