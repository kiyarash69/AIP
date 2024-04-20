from django.urls import path
from .views import BlogClassView

app_name = 'blog-app'
urlpatterns = [
    path(
        '', BlogClassView.as_view(), name='main-page-blog'
    ),
]
