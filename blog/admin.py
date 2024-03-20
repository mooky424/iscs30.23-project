# Register your models here.

from django.contrib import admin
from .models import ArticleCategory, Article

class ArticleCategoryInline(admin.TabularInline):
    model = ArticleCategory

class ArticleInline(admin.TabularInline):
    model = Article

admin.site.register(ArticleCategory)
admin.site.register(Article)


