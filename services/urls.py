from django.urls import path
from .views import *

app_name = 'services_app'
urlpatterns = [
    path('', CoursesView.as_view(), name='services_main_page'),
    path('innovation', InnovationClassView.as_view(), name='innovation'),  # this code is rendering innovation.html

]
