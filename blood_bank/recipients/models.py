from django.db import models
from users.models import CustomUser

class Recipient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    required_blood = models.CharField(max_length=3)
    urgency_level = models.CharField(max_length=10, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ])

    def __str__(self):
        return f"{self.user.username} - {self.required_blood}"
