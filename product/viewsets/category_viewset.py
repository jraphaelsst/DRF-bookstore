from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from product.models import Category
from product.serializers import CategorySerializer

class CategoryViewSet(ModelViewSet):
    authentication_classes = [BasicAuthentication, TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = CategorySerializer
    #queryset = Product.objects.all()
    
    def get_queryset(self):
        return Category.objects.all().order_by('id')
