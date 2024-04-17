from django.urls import path
from .views import *

app_name = 'services_app'
urlpatterns = [
    path('', CoursesView.as_view(), name='services_main_page'),
]
