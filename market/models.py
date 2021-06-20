from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class market(models.Model):
    choice = [
        ('n', 'nishant'),
        ('a', 'anurag'),
    ]

    Name = models.CharField(max_length=50)
    Status = models.CharField(max_length=2, choices='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    Class = models.CharField(max_length=2, choices='')
