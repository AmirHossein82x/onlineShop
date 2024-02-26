from rest_framework import routers
from config.apps.catalog.views.admin import CategoryViewSet

router = routers.SimpleRouter()
router.register('categories', CategoryViewSet, basename='category')

urlpatterns = [] + router.urls