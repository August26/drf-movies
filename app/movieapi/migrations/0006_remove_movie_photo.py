# Generated by Django 2.2.1 on 2020-02-02 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapi', '0005_movie_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='photo',
        ),
    ]
