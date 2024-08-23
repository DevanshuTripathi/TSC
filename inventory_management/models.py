from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission 

# Create your models here.
class User(AbstractUser):
    
    groups = models.ManyToManyField(
        Group,
        related_name='inventory_user_set',  # Customize the related name here
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='inventory_user_permissions_set',  # Customize the related name here
        blank=True,
    )