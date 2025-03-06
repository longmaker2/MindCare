from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Question, Video
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
        fields = ["professional_name", "date", "time", "reason"]  # Ensure only valid fields are here

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
from django import forms
from .models import Book

class BookUploadForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "pdf_file"]
from django import forms
from .models import Quiz

from django import forms
from .models import Quiz

class QuizForm(forms.ModelForm):
    """ Form to create a quiz. """
    class Meta:
        model = Quiz
        fields = ['title', 'description', 'category']  # Only relevant fields
class QuestionForm(forms.ModelForm):
    """Form to create quiz questions with options as JSON."""
    options = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), help_text="Enter options as a comma-separated list.")
    
    class Meta:
        model = Question
        fields = ['text', 'options', 'correct_answer']

    def clean_options(self):
        """Ensure options are stored as a JSON list."""
        options = self.cleaned_data['options']
        options_list = [option.strip() for option in options.split(',')]
        if len(options_list) < 2:
            raise forms.ValidationError("You must provide at least two options.")
        return options_list  # Store as a list instead of string
