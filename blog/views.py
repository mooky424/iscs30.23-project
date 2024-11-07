from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, View

from .forms import CommentForm
from .models import Article, ArticleCategory, Comment


# Create your views here.
class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        context["comments"] = self.object.article_comment.all()

        author_articles = Article.objects.filter(author=self.object.author).exclude(
            pk=self.object.pk
        )[:2]
        context["author_articles"] = author_articles

        return context

    def post(self, request, *args, **kwargs):
        comment = CommentForm(request.POST).save(commit=False)
        article_pk = self.get_object().pk
        comment.author = self.request.user.profile
        comment.article = Article.objects.get(pk=article_pk)
        comment.save()

        return self.get(request, *args, **kwargs)


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "blog/article_list.html"
    context_object_name = "articles"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_articles = Article.objects.filter(author=self.request.user.profile)
        other_articles = Article.objects.exclude(author=self.request.user.profile)
        categories = ArticleCategory.objects.all()

        context["other_articles"] = other_articles
        context["user_articles"] = user_articles
        context["categories"] = categories
        return context


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user.profile
            comment.save()
        return redirect("blog:article_detail", pk=pk)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "blog/article_form.html"
    fields = ["title", "category", "entry", "header_image"]
    success_url = reverse_lazy("blog:blog")

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = "blog/article_form.html"
    fields = ["title", "category", "entry", "header_image"]

    def get_success_url(self):
        return reverse_lazy("blog:article_detail", kwargs={"pk": self.object.pk})
