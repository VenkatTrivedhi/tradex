from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=10,decimal_places=2)
    price = models.DecimalField(max_digits=15,decimal_places=2)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True)

