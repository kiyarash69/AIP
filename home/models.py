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


SKILLS_CHOICES = [
    ('developer', 'Developer'),
    ('django', 'Django'),
    ('css', 'CSS'),
    ('html', 'HTML'),
    ('git', 'Git'),
    ('python', 'Python'),
    ('machine_learning', 'Machine Learning'),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/')
    skills = models.CharField(max_length=50, choices=SKILLS_CHOICES)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    telegram = models.CharField(max_length=50, blank=True, null=True)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    gmail = models.EmailField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
