from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile_images', default='profile_img.jpg')
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
    