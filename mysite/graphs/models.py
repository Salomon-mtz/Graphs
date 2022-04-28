from django.db import models

class Player(models.Model):
    first_name = models.CharField(max_length=20, default=0)
    username = models.CharField(max_length=20, default=0)
    email = models.CharField(max_length=30, default=0)
    password = models.CharField(max_length=20, default=0)
    level = models.IntegerField(default=1)
    country = models.CharField(max_length=50, default=0)
