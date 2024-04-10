from django.shortcuts import render
from .models import WhyAi
from django.views.generic import TemplateView

from django.views.generic import TemplateView
from .models import WhyAi


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch data from the WhyAi model and add it to the context
        context['data'] = WhyAi.objects.all()

        return context
