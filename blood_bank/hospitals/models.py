from django.db import models
from users.models import CustomUser

class Hospital(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_person = models.CharField(max_length=255)

    def __str__(self):
        return self.name
