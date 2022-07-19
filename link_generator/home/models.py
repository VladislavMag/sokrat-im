from django.core.validators import MaxLengthValidator
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Link(models.Model):
    link = models.CharField('Your link', max_length=500, validators=[
            MaxLengthValidator(250)])
    title = models.CharField('Short link', max_length=100, unique=True)
    avtor = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('link')


    def __str__(self):
        return self.title
