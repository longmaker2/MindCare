from django.db import models
from .validators import file_size
from django.contrib.auth.models import User


# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)


class Chart(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)

class Video(models.Model):
    caption=models.CharField(max_length=10000)
    video=models.FileField(upload_to="Video/",validators=[file_size])
    def __str__(self):
        return self.caption

class MentorshipApplication(models.Model):
     field1 = models.CharField(max_length=100)
     field2 = models.TextField()
     field3 = models.IntegerField()
    # ... other fields
     def __str__(self):
        return self.field1
     

from django.db import models
from django.contrib.auth.models import User

class Professional(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    contact_email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    image = models.ImageField(upload_to='professionals/', null=True, blank=True)
    available_slots = models.JSONField(default=list)  # Store slots as a JSON list

    def __str__(self):
        return self.name

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()  # Correct format HH:MM:SS
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.professional.name} - {self.date} {self.time}"

from django.db import models
from django.utils.timezone import now

class ChatMessage(models.Model):
    username = models.CharField(max_length=50, default="Anonymous")
    content = models.TextField()
    timestamp = models.DateTimeField(default=now)  # Automatically set timestamp

    def __str__(self):
        return f"{self.username}: {self.content[:50]}"
