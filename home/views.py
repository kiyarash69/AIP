from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView

from django.views.generic import TemplateView
from .models import WhyAi


class IndexView(TemplateView):  # render index.html and send data for it
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch data from the WhyAi model and add it to the context
        context['data'] = WhyAi.objects.all()

        return context


class OurServiceView(TemplateView):  # send data for OurService.html in the includes
    template_name = 'includes/Our-service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['data'] = OurService.objects.all()
        return context


class DailyNewsView(TemplateView):  # for send data to includes/DailyNews.html
    template_name = 'includes/DailyNews.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['data'] = DailyNews.objects.all()
        return context


class FooterView(TemplateView):  # send data for footer.html in the includes
    template_name = 'includes/footer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['data'] = OurService.objects.all()
        return context


# <=====================================================================================================================>


class AboutClassView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve profile data
        try:
            profile = Profile.objects.get(user=self.request.user)
            context['profile'] = profile
        except Profile.DoesNotExist:
            context['profile'] = None

        # Retrieve data from WhyAi model
        context['data'] = WhyAi.objects.all()

        return context
