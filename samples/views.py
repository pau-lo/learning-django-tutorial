from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Article


# class HomePageView(TemplateView):
# template_name = 'home.html'

class HomePageView(ListView):
    model = Article
    template_name = 'home.html'
    context_object_name = 'all_articles_list'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'add_article.html'
    fields = ['title', 'author', 'text', 'photo']


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ['title', 'text']


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('home')


class AboutPageView(TemplateView):
    template_name = 'about.html'
