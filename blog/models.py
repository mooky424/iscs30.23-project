from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    entry_field = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    categories = models.ForeignKey(
        "ArticleCategory", on_delete=models.SET_NULL, null=True, related_name="articles"
    )
    header_image = models.ImageField(upload_to="article_images", default="default.jpg")

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:article_detail", args=[str(self.pk)])


class ArticleCategory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "article categories"

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    entry_field = models.TextField()

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
