from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DonationHistoryViewSet

router = DefaultRouter()
router.register(r'', DonationHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
