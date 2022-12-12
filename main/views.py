from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ProductSerializer,CategorySerializer
from .models import Category,Product
from .filters import ProductFilter


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    # filterset_fields = ['category','status']

    def get_permissions(self):
        if self.action in ['retrieve','list','search']:
            #если это запрос на листинг или на детализацию 
            return [] # разрешаем всем
        return [IsAdminUser()] # разрешаем только админам

    @action(['GET'], detail=False)
    def search(self, request):
        # /products/search/?q=hello
        #query_params = {'q':'hello'}
        q = request.query_params.get('q')
        #get_queryset - Product.objects.all()
        queryset=self.get_queryset()
        if q:
            # queryset = queryset.filter(title__icontains = q) # title ilike '%hello%'
            queryset = queryset.filter(Q(title__icontains=q)| Q(description__icontains=q))
            # title ilike '%hello%' or description ilike '%hello%'
        # get_serializer - ProductSerializer
        
        pagination = self.paginate_queryset(queryset)
        if pagination:
            serializer = self.get_serializer(pagination, many = True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many = True)
        return Response(serializer.data,status=200)



