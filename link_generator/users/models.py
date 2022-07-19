from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Інформація про {self.user.username}'


    class Meta:
        verbose_name = 'Профіль'
        verbose_name_plural = 'Профілі'
