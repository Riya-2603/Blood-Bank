from rest_framework import viewsets
from .models import DonationHistory
from .serializers import DonationHistorySerializer

class DonationHistoryViewSet(viewsets.ModelViewSet):
    queryset = DonationHistory.objects.all()
    serializer_class = DonationHistorySerializer
