from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView
from .models import Article
from home.models import Profile


class BlogClassView(ListView):
    model = Article
    template_name = 'blog.html'


class BlogDetailClassView(DetailView):
    model = Article
    template_name = 'Article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()  # Retrieve the current article
        context['profile'] = get_object_or_404(Profile,
                                               user=article.author)
        return context
