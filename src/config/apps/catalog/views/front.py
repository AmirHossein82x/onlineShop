from rest_framework.viewsets import ReadOnlyModelViewSet

from config.apps.catalog.models import Category
from config.apps.catalog.serializers.front import CategorySerializer


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
