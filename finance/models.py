from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    pass

class Finance (models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_finances")
    income = models.DecimalField(max_digits=10, decimal_places=2)