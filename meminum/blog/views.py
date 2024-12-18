# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Article
from .forms import ArticleForm

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/home.html'
    context_object_name = 'articles'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html'

class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html'

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('home')
    template_name = 'blog/article_confirm_delete.html'

def profile(request):
    articles = Article.objects.all()  
    return render(request, 'blog/profile.html', {'articles': articles})
