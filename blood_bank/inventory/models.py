from django.db import models

class BloodInventory(models.Model):
    blood_group = models.CharField(max_length=3, unique=True)
    units_available = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.blood_group}: {self.units_available} units"
