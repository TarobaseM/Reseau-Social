# Generated by Django 4.2.6 on 2023-10-23 23:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PostApp', '0013_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(null=True, related_name='liked_publications', to=settings.AUTH_USER_MODEL),
        ),
    ]