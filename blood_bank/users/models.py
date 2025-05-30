from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('donor', 'Donor'),
        ('recipient', 'Recipient'),
        ('hospital', 'Hospital'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    location = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.username} ({self.role})"
