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
     

from django.contrib.auth.models import User
from django.db import models

class Professional(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    contact_email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    image = models.ImageField(upload_to='professionals/', null=True, blank=True)
    available_slots = models.JSONField(default=list)  # Store available slots as a JSON list
    booked_slots = models.JSONField(default=list)  # Store booked slots as a JSON list

    def __str__(self):
        return self.name


from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Ensuring user is linked to appointment
    professional = models.ForeignKey('Professional', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment with {self.professional.name} on {self.date} at {self.time}"

class ChatMessage(models.Model):
    content = models.TextField()
    username = models.CharField(max_length=100, default="Anonymous")
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # Remove `room_id` completely if not needed
    # room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, null=True, blank=True)  # Remove this if unused

    def __str__(self):
        return f"{self.username}: {self.content[:50]}"

from django.db import models

class Video(models.Model):
    CATEGORY_CHOICES = [
        ('Anxiety', 'Anxiety'),
        ('Depression', 'Depression'),
        ('PTSD', 'Post-Traumatic Stress Disorder'),
    ]

    title = models.CharField(max_length=255, null=True, blank=True)  # Ensure it allows null values
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=True, blank=True)
    video_file = models.FileField(upload_to="videos/", null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    caption = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title if self.title else "Untitled Video"
    

    