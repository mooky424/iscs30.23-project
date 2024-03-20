from django.db import models
from django.urls import reverse


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    ordering = ['name']


    def __str__(self):
        return self.name
   
    def get_absolute_url(self):
        return reverse('wiki/articles', args=str(self.pk))


class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null=True)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add="True")
    updated_on = models.DateTimeField(auto_now="True")
    ordering = ["-created_on"]
   
    def __str__(self):
        return self.name
   
    def get_absoulute_url(self):
        return reverse('wiki/article/1', args=str(self.pk))