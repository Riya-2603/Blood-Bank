from django.db import models
from users.models import CustomUser

class BloodRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3)
    units_requested = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    request_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Request by {self.user.username} - {self.blood_group} - {self.status}"
