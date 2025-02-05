from django.contrib.auth.models import User
from django.db import models
from birthday import BirthdayField, BirthdayManager


class WhyAi(models.Model):
    title = models.CharField(max_length=100)  # this section is for index.html 'why artificial intelligence'
    description = models.TextField()

    def __str__(self):
        return self.title


class OurService(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='home/services/image', blank=True, null=True)

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
    ('FrontEnd', 'Front End'),
    ('BackEnd', 'Back End'),
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles')
    image = models.ImageField(upload_to='profile_images/')
    about_me = models.TextField()
    skills = models.CharField(max_length=50, choices=SKILLS_CHOICES)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    telegram = models.CharField(max_length=50, blank=True, null=True)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    gmail = models.EmailField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    birthday = BirthdayField()
    objects = BirthdayManager()

    def __str__(self):
        return f"Profile of {self.user.username}"


class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"contact of {self.name}"
