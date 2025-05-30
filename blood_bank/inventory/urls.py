from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BloodInventoryViewSet

router = DefaultRouter()
router.register(r'', BloodInventoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
