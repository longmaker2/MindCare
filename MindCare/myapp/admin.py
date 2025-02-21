from django.contrib import admin
from .models import (
    Feature, Chart, Video, Book, Article, Course, Quiz, 
    AnonymousPrivateMessage, Appointment, CompletedCourse, 
    Professional, Message
)

# Register your models
admin.site.register(Feature)
admin.site.register(Chart)
admin.site.register(Video)
admin.site.register(Book)
admin.site.register(Article)
admin.site.register(Course)
admin.site.register(Quiz)
admin.site.register(AnonymousPrivateMessage)
admin.site.register(Appointment)
admin.site.register(CompletedCourse)
admin.site.register(Professional)
admin.site.register(Message)
