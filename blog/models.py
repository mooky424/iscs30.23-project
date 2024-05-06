from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=255)
    entry_field = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    categories = models.ForeignKey(
        "ArticleCategory", on_delete=models.SET_NULL, null=True, related_name="articles"
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:article_detail", args=[str(self.pk)])


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "article categories"

    def __str__(self):
        return self.name
