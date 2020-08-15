from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    pass

class Percentages (models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_percentages")
    tax_rate= models.DecimalField(max_digits=10, decimal_places=5, default=0.005)
    emergency = models.DecimalField(max_digits=10, decimal_places=4, default=0.1)
    insurance = models.DecimalField(max_digits=10, decimal_places=4, default=0.2)
    pension = models.DecimalField(max_digits=10, decimal_places=4, default=0.2)
    spending = models.DecimalField(max_digits=10, decimal_places=4, default=0.495)

class Finance (models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_finances")
    income = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    tax = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    emergency = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    insurance = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    pension = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    spending = models.DecimalField(max_digits=12, decimal_places=2, null=True)