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
