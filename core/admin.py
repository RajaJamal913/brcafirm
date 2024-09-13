# contact/admin.py
from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'sent_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('sent_at',)
