from django.contrib import admin
from .models import Room, Message

# Register your models here.
admin.site.register(Room)
admin.site.register(Message)
from django.contrib import admin
from myapp.models import Professional  # ✅ Correct


@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'contact_email', 'phone_number')
