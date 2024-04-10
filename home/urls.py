from django.urls import path
from .views import *

app_name = 'home_app'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # this address is for Index.html
    path('Ourservice', OurServiceView.as_view(), name='OurService_partial'),  # this address is for includes/OurService.html
]
