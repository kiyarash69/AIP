from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(blank=True, null=True, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='home/services/image', blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.create_at:
            self.create_at = timezone.now()
        super().save()


print('-------------------------------------------------------------------------------------------------------')

List = [
    ('finance', 'Finance'),
    ('machine-learning', 'Machine-learning'),
    ('robotic', 'Robotic'),
    ('search-AI', 'Search AI'),
]


class InnovationModel(models.Model):
    filter = models.CharField(max_length=100, choices=List)
    image = models.ImageField(upload_to='image/innovation/')
    description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return f'{self.filter} , {self.id}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)
