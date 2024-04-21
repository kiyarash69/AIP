from django.urls import path
from .views import *

app_name = 'blog-app'
urlpatterns = [
    path(
        '', BlogClassView.as_view(), name='main-page-blog'
    ),
    path(
        'detail/<slug:slug>', BlogDetailClassView.as_view(), name='detail-page-blog'
    ),
]
