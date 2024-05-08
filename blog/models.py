from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
<<<<<<< HEAD
from user_management.models import Profile

class ArticleCategory(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(null = True, blank = True)
=======


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        "ArticleCategory", on_delete=models.SET_NULL, null=True, related_name="articles"
    )
    header_image = models.ImageField(upload_to="article_images", default="default.jpg")

    class Meta:
        ordering = ["-created_on"]

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
        ordering = ["title"]
        verbose_name_plural = "article categories"
>>>>>>> main

    def __str__(self):
        return self.name

<<<<<<< HEAD
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
=======

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    entry = models.TextField()

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
>>>>>>> main
