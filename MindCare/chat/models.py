from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
  name = models.CharField(max_length=1000)
class Message(models.Model):
  value = models.CharField(max_length=1000000)
  date = models.DateTimeField(default=datetime.now, blank=True)
  user = models.CharField(max_length=1000000)
  room = models.CharField(max_length=1000000)

from django.db import models
from django.contrib.auth.models import User

class Professional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    available_slots = models.JSONField(default=list)  # Store available slots as a list

    def __str__(self):
        return self.name