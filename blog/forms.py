from django import forms
from .models import Article, ArticleCategory, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields =  '__all__'
        widgets = {
            "category" : forms.Select()
        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args,**kwargs)
            self.fields['author'].disabled = True

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']
        widgets = {
            "entry" : forms.Textarea()
        }