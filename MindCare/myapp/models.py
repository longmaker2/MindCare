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
from django.db import models
from django.contrib.auth.models import User

class Professional(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='professionals/', blank=True, null=True)

    # New field: Available time slots
    available_times = models.JSONField(default=list)  # Example: ["09:00", "10:00", "11:00"]

    def __str__(self):
        return self.name


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()  # ✅ Ensure this field exists
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

     


    