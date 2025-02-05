from django.db import models
from .validators import file_size

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

class Professional(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=255)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(upload_to='professionals/', default='default.jpg')

    def __str__(self):
        return self.name

     



    