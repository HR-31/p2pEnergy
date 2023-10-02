from django.db import models

class EnergyResource(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)  # Renewable energy source type
    price_per_kw = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=50)
    quantity_kw = models.DecimalField(max_digits=10, decimal_places=2)
