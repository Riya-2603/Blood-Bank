from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from .views import ProtectedView

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('profile/', ProtectedView.as_view()),
]
