from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission 

# Create your models here.
class User(AbstractUser):
    pass

class Item(models.Model):
    company = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company} {self.name} {self.type}"

