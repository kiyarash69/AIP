from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import InnovationModel, Service


class ServiceClassView(TemplateView):
    template_name = 'services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Service.objects.all()
        return context


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service_detail.html'


# class InnovationClassView(TemplateView):
#     template_name = 'innovation.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['data'] = InnovationModel.objects.all()
#         return context

class InnovationClassView(TemplateView):
    template_name = 'innovation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the filter category from the URL or request parameters
        filter_category = self.request.GET.get('category')

        # Filter data based on the selected category
        if filter_category:
            context['data'] = InnovationModel.objects.filter(filter=filter_category)
        else:
            context['data'] = InnovationModel.objects.all()

        return context

