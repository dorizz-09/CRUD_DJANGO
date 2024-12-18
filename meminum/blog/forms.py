# blog/forms.py
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'image', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title...'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description...', 'rows': 3}),
            'content': forms.Textarea(attrs={'placeholder': 'Article...'}),
        }