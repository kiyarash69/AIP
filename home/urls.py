from django.urls import path
from .views import *

app_name = 'home_app'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # this address is for Index.html
    path('Ourservice', OurServiceView.as_view(), name='OurService_partial'),
    # this address is for includes/OurService.html
    path('DailyNews', DailyNewsView.as_view(), name='DailyNews_partial'),  # this address is for includes/DailyNews.html
    path('Footer', FooterView.as_view(), name='footer_partial'),  # this address is for includes/footer.html
    path('about', AboutClassView.as_view(), name='about'),  # this address is for about.html
]
