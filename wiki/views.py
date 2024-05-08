from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.http import HttpResponseRedirect

from user_management.models import Profile

from .models import Article, ArticleCategory, Comment
from .forms import ArticleForm, CommentForm


class ArticleList(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "wiki/article_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article_category"] = ArticleCategory.objects.all()
        return context


class ArticleDetail(DetailView):
    model = Article
    context_object_name = "article"
    template_name = "wiki/article_detail.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["article_category"] = ArticleCategory.objects.all()
        ctx["comments"] = Comment.objects.all()
        ctx["form"] = CommentForm()
        return ctx

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            comment.author = Profile.objects.get(user = self.request.user)
            comment.article = self.get_object()
            comment.entry = form.cleaned_data.get('entry')
            comment.save()
            return HttpResponseRedirect(request.path)
        else: 
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context["form"] = form 
            return self.render_to_response(context)


class ArticleCreate(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "wiki/article_form.html"

    def get_initial(self):
        author = Profile.objects.get(user=self.request.user)
        return {'author': author}

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["categories"] = ArticleCategory.objects.all()
        return ctx

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("wiki:article", kwargs={'pk':self.object.pk})


class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = ""

    template_name = "wiki/article_form.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["categories"] = ArticleCategory.objects.all()
        ctx["form"] = ArticleForm()
        return ctx
    
    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("wiki:article", kwargs={'pk':self.object.pk})
