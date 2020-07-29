from django.contrib import admin
from .models import Email

class EmailAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'sender_email', 'subject', 'origin', 'arrived_at')
    list_filter = ('sender_name', 'sender_email')

# Register your models here.
admin.site.register(Email, EmailAdmin)
