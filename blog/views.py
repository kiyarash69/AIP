from django.shortcuts import redirect, render
from django.urls import reverse
from home.models import Profile
from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404
from .models import Article, Comment
from .forms import CommentForm


class BlogClassView(ListView):
    model = Article
    template_name = 'blog.html'
    paginate_by = 2


class BlogDetailClassView(DetailView):
    model = Article
    template_name = 'Article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        context['profile'] = get_object_or_404(Profile, user=article.author)
        context['comment_form'] = CommentForm()
        context['parent_comment_id'] = self.request.GET.get('parent_comment_id')  # Pass parent_comment_id to template
        return context

    def post(self, request, *args, **kwargs):
        article = self.get_object()
        form = CommentForm(request.POST)
        parent_comment_id = request.POST.get('parent_comment_id')  # Retrieve parent_comment_id from form
        if form.is_valid():
            parent_comment = None
            if parent_comment_id:
                parent_comment = get_object_or_404(Comment, id=parent_comment_id)
            comment = form.save(commit=False)
            comment.post = article
            comment.user = request.user
            comment.parent = parent_comment
            comment.save()
            return redirect(reverse('blog-app:detail-page-blog', kwargs={'slug': article.slug}))
        else:
            return redirect(reverse('blog-app:detail-page-blog'))
            pass

        return redirect(reverse('blog-app:detail-page-blog', kwargs={'slug': article.slug}))


class SearchArticleListView(ListView):
    model = Article
    template_name = 'blog.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Article.objects.filter(title__icontains=query)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        context['search_query'] = query
        return context

    def get_template_names(self):
        queryset = self.get_queryset()
        if not queryset.exists():
            return ['error.html']  # Template for no results
        else:
            return [self.template_name]
