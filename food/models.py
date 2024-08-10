from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='items', default="")

    def __str__(self):
        return self.name 