from django import forms
from .models import Article, ArticleCategory, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry', 'header_image']
        widgets = {
            "category": forms.Select()
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["entry"]
        widgets = {
            "entry" : forms.Textarea()
        }