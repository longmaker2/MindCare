from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Video
from .models import MentorshipApplication
from .models import Professional


class Video_form(forms.ModelForm):
  class Meta:
    model=Video
    fields=("caption","video")

class MentorshipApplicationForm(forms.ModelForm):
    class Meta:
        model = MentorshipApplication
        fields = ('field1', 'field2')


from django import forms
from .models import Professional

class ProfessionalForm(forms.ModelForm):
    class Meta:
        model = Professional
        fields = ['name', 'image', 'specialty', 'contact_email', 'phone_number']  # Ensure these exist in models.py


from myapp.models import Professional


#from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["professional", "date", "time", "reason"]  # Ensure only valid fields are here

from django import forms
from .models import Video

class VideoUploadForm(forms.ModelForm):  # Renamed to follow naming conventions
    class Meta:
        model = Video
        fields = ['title', 'category', 'video_file', 'video', 'caption']

from django import forms
from .models import Book, Article, Course

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'pdf_file']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'summary', 'url']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'level', 'url']
