# Generated by Django 2.2.1 on 2020-02-04 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('id_film', models.IntegerField(blank=True, default=0)),
                ('photo', models.CharField(blank=True, max_length=500)),
                ('city_films', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='movieapi.Cities')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=50)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('id_film', models.IntegerField(blank=True, default=0)),
                ('place', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('session', models.CharField(choices=[('2D', '2D'), ('3D', '3D'), ('3DX', '3DX'), ('imax', 'IMAX')], default='2D', max_length=4)),
                ('time_session', models.CharField(blank=True, max_length=100)),
                ('data_session', models.CharField(blank=True, max_length=100)),
                ('price', models.IntegerField(blank=True, default=0)),
                ('photo', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_session', models.CharField(blank=True, max_length=15)),
                ('film_presentation', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='movieapi.Films')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('session', models.CharField(choices=[('2D', '2D'), ('3D', '3D'), ('3DX', '3DX'), ('imax', 'IMAX')], default='2D', max_length=4)),
                ('time_session', models.CharField(blank=True, max_length=100)),
                ('price', models.IntegerField(blank=True, default=0)),
                ('presentation_info', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='movieapi.Presentation')),
            ],
        ),
    ]
