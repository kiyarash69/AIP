# Generated by Django 5.0.4 on 2024-04-16 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_profile_gmail_profile_linkedin_profile_telegram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourservice',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='home/services/image'),
        ),
    ]