# contact/forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 5:
            raise forms.ValidationError("Message should be at least 5 characters long.")
        return message
