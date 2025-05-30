from django.db import models
from users.models import CustomUser

class Donor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3)
    last_donation_date = models.DateField(null=True, blank=True)
    eligibility_status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.blood_group}"
