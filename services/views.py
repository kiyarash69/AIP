from django.shortcuts import render
from django.views.generic import TemplateView
from home.models import OurService


class CoursesView(TemplateView):
    template_name = 'services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['courses'] = OurService.objects.all()
        return context
