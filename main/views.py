from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer,CategorySerializer
from .models import Category,Product


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer