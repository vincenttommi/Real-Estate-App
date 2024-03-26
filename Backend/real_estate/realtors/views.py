from rest_framework.generics  import ListAPIView,RetrieveAPIView
from rest_framework import permissions
from  .models import Realtor
from .serializers import  RealtorSerializer


class  RealtorListView(ListAPIView):
    #is accessible without any authentication or permission,allows any user to sign up
    permission_classes  = (permissions.AllowAny,)
    
    queryset = Realtor.objects.all()
    #query to retrieve  realtor objects from database
    serializer_class = RealtorSerializer
    pagination_class = None
    #spliting individual pages of data
    
    
    
    
class RealtorView(RetrieveAPIView):
    queryset =  Realtor.objects.all()
    #getting objects from Realtor 
    serializer_class = RealtorSerializer
    
    
    
class TopSellerView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    
    
    queryset = Realtor.objects.filter(top_seller=True)
    #filtering the top seller where the attribute is equal to True 
    serializer_class = RealtorSerializer
    pagination_class = None
    
        
    
    