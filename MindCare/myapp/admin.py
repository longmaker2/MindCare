from django.contrib import admin
from .models import Feature
from .models import Chart
from .models import Video
from .models import Book, Article, Course  # Import your models
from .models import Quiz
from .models import AnonymousPrivateMessage

admin.site.register(Quiz)

admin.site.register(Book)
admin.site.register(Article)
admin.site.register(Course)

# Register your models here.
admin.site.register(Feature)
admin.site.register(Chart)
admin.site.register(Video)
admin.site.register(AnonymousPrivateMessage)
