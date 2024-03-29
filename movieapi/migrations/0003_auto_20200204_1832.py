# Generated by Django 2.2.1 on 2020-02-04 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieapi', '0002_auto_20200204_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='presentation_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapi.Presentation'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='film_presentation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapi.Films'),
        ),
    ]
