from ..models import Category
from rest_framework import viewsets
from ..serializers.admin import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
