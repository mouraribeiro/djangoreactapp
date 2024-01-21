from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class List(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    done = models.BooleanField()

    def __str__(self):
        return self.name

