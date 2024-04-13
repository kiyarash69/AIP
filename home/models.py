from django.contrib.auth.models import User
from django.db import models


class WhyAi(models.Model):
    title = models.CharField(max_length=100)  # this section is for index.html 'why artificial intelligence'
    description = models.TextField()

    def __str__(self):
        return self.title


class OurService(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class DailyNews(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Daily')
    image = models.ImageField(upload_to='images/DailyNews/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


