from django.shortcuts import render
from django.views.generic import TemplateView


class BlogClassView(TemplateView):
    template_name = 'blog.html'
