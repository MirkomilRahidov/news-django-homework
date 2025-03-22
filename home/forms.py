from django import forms
from .models import ContactMessage
from users.models import Comment

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'text']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  
