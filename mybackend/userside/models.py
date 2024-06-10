# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)  # Define the phone field
    image = models.ImageField(upload_to='images/',null=True,blank=True)



