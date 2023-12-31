# Generated by Django 4.2.4 on 2023-10-16 14:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PostApp', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='liked_publications', to=settings.AUTH_USER_MODEL),
        ),
    ]
