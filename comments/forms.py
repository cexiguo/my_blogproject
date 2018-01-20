from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """docstring for forms.ModelForm"""
    class Meta:
        model = Comment
        fields = ['name','email','url','text']
