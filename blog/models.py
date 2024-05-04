from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/blogs')
    image_list = models.ImageField(upload_to='images/blogs', blank=True, null=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[:30]


class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    create_on = models.DateTimeField(auto_now_add=True, verbose_name="Created On")
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['create_on']

    def __str__(self):
        return 'Comment "{}" by {}'.format(self.body, self.user)
