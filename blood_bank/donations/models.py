from django.db import models
from users.models import CustomUser

class DonationHistory(models.Model):
    donor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    units_donated = models.PositiveIntegerField()
    donation_date = models.DateField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.donor.username} - {self.units_donated} units"
