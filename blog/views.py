from .models import Article
from django.views.generic import ListView, DetailView

# Create your views here.
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"