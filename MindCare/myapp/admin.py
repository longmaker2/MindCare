from django.contrib import admin
from .models import (
    Feature, Chart, Video, Book, Article, Course, 
    AnonymousPrivateMessage, Appointment, CompletedCourse, 
    Professional, Message
)
from django.contrib import admin
from .models import Quiz, Question

# Register your models
admin.site.register(Feature)
admin.site.register(Chart)
admin.site.register(Video)
admin.site.register(Book)
admin.site.register(Article)
admin.site.register(Course)
#admin.site.register(Quiz)
admin.site.register(AnonymousPrivateMessage)
admin.site.register(Appointment)
admin.site.register(CompletedCourse)
admin.site.register(Professional)
admin.site.register(Message)

class QuestionInline(admin.TabularInline):  # Allows adding questions inside quizzes
    model = Question
    extra = 5  # Show 5 empty question fields

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title',)
    inlines = [QuestionInline]  # Link questions to quizzes in admin panel

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz', 'correct_answer')
    list_filter = ('quiz',)
