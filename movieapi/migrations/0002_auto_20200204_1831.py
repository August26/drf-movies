# Generated by Django 2.2.1 on 2020-02-04 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='city_films',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapi.Cities'),
        ),
    ]
