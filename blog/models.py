from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from user_management.models import Profile

class ArticleCategory(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["name"]


class Article(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(
        Profile,
        on_delete = models.SET_NULL,
        null = True,
    )

    category = models.ForeignKey(
        ArticleCategory, 
        on_delete = models.SET_NULL, 
        null = True, 
        related_name = "article_category"
        )

    entry = models.TextField(null = True, blank = True)
    header_image = models.ImageField(upload_to = "images/blog", null = True)
    created_on = models.DateTimeField(null = False, editable = False, auto_now_add = True)
    updated_on = models.DateTimeField(null = True, editable = False, auto_now = True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:article_detail', args = [self.pk])
    
    class Meta:
        ordering = ["-updated_on"]


class Comment(models.Model):
    author = models.ForeignKey(
        Profile,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        related_name = 'comment_author'
    )

    article = models.ForeignKey(
        Article,
        on_delete = models.CASCADE,
        null = True,
        blank = True,
        related_name = 'comment_article'
    )

    entry = models.TextField(null=True)
    created_on = models.DateTimeField(null = False, auto_now_add = True)
    updated_on = models.DateTimeField(null = True, auto_now = True)

    def __str__(self):
        return f"Comment by {self.author} on {self.article.title}"
    
    class Meta:
        ordering = ["-created_on"]
