from rest_framework import viewsets
from .models import BloodInventory
from .serializers import BloodInventorySerializer

class BloodInventoryViewSet(viewsets.ModelViewSet):
    queryset = BloodInventory.objects.all()
    serializer_class = BloodInventorySerializer
