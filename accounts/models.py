from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number =models.CharField(max_length=15 ,blank=True , null= True)

    def __str__(self):
        return self.username

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='addresses')
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    building_number = models.CharField(max_length=50)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.city} - {self.street} ({self.user.username})"