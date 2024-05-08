from django.shortcuts import render, redirect
from .models import *
from django.views.generic import TemplateView, View
from .forms import ContactForm
from .models import WhyAi, Profile, ContactModel


class IndexView(TemplateView):  # render index.html and send data for it
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch data from the WhyAi model and add it to the context
        context['data'] = WhyAi.objects.all()

        return context


# <=====================================================================================================================>


class OurServiceView(TemplateView):  # send data for OurService.html in the includes
    template_name = 'includes/Our-service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['data'] = OurService.objects.all()
        return context


# <=====================================================================================================================>


class DailyNewsView(TemplateView):  # for send data to includes/DailyNews.html
    template_name = 'includes/DailyNews.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['data'] = DailyNews.objects.all()
        return context


# <=====================================================================================================================>


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
        profile = Profile.objects.all()
        context['profile'] = profile
        context['data'] = WhyAi.objects.all()

        return context


class TeamClassView(TemplateView):
    template_name = 'team.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Profile.objects.all()
        return context


# <=====================================================================================================================>


class ContactClassBaseView(View):

    def get(self, request):
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            title = form.cleaned_data.get('title')
            email = form.cleaned_data.get('email')
            description = form.cleaned_data.get('description')
            ContactModel.objects.create(name=name, title=title, email=email, description=description)
            return redirect('home_app:contact')
        else:
            form = ContactForm()
        return render(request, 'contact.html')
