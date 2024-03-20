from django.shortcuts import render
from .models import Article
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
