# Generated by Django 5.0.4 on 2024-04-14 12:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_dailynews'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profile_images/')),
                ('skills', models.CharField(choices=[('developer', 'Developer'), ('django', 'Django'), ('css', 'CSS'), ('html', 'HTML'), ('git', 'Git'), ('python', 'Python'), ('machine_learning', 'Machine Learning')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]