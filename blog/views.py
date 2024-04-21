from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Article


class BlogClassView(ListView):
    model = Article
    template_name = 'blog.html'


class BlogDetailClassView(DetailView):
    model = Article
    template_name = 'Article_detail.html'
