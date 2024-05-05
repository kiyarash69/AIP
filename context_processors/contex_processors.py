from django.views.generic import TemplateView
from blog.models import Article
from home.models import OurService


def recent_articles(request):
    recent_articles = Article.objects.order_by('-updated_at')
    our_service = OurService.objects.all()

    return {'recent_article': recent_articles, 'our_service': our_service}
