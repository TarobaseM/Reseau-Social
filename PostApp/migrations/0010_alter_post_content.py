# Generated by Django 4.2.6 on 2023-10-16 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostApp', '0009_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=1000),
        ),
    ]
