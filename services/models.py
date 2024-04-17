from django.db import models
from django.utils import timezone

List = [
    ('finance', 'Finance'),
    ('machin learning', 'Machin learning'),
    ('robotic', 'Robotic'),
    ('search AI', 'Search AI'),
]


class InnovationModel(models.Model):
    filter = models.CharField(max_length=100, choices=List)
    image = models.ImageField(upload_to='image/innovation/')
    description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return f'{self.filter} , {self.id}'
