from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipientViewSet

router = DefaultRouter()
router.register(r'', RecipientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
