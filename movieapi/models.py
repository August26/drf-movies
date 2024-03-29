from django.db import models


class Movie(models.Model):

    Session = (
        ('2D', '2D'),
        ('3D', '3D'),
        ('3DX', '3DX'),
        ('imax', 'IMAX'))
    city = models.CharField(blank=True, max_length=50)
    title = models.CharField(blank=True, max_length=100)
    id_film = models.IntegerField(blank=True, default=0)
    place = models.CharField(blank=True, max_length=100)
    address = models.CharField(blank=True, max_length=100)
    session = models.CharField(max_length=4, choices=Session, default='2D')
    time_session = models.CharField(blank=True, max_length=100)
    data_session = models.CharField(blank=True, max_length=100)
    price = models.IntegerField(blank=True, default=0)
    photo = models.CharField(blank=True, max_length=500)
    # photo = models.ImageField(upload_to='photos', height_field=None, width_field=None, max_length=100, default='none')
    # tasks = models.ForeignKey(Notebook, null=True, blank=True, related_name='tasks', on_delete=models.CASCADE,
    #                           default='')

    def __str__(self):
        return self.title


class City(models.Model):

    city = models.CharField(blank=True, max_length=50, unique=True)
    cookie = models.CharField(blank=True, max_length=2000)

    def __str__(self):
        return self.city


class Film(models.Model):

    title = models.CharField(blank=True, max_length=100)
    id_film = models.IntegerField(blank=True, default=0)
    photo = models.CharField(blank=True, max_length=500)
    city_film = models.ForeignKey(City, on_delete=models.CASCADE, related_name="films")

    def __str__(self):
        return self.title


class Presentation(models.Model):

    data_session = models.CharField(blank=True, max_length=15)
    film_presentations = models.ForeignKey(Film, on_delete=models.CASCADE, related_name="presentations")

    def __str__(self):
        return self.data_session


class Info(models.Model):

    Session = (
        ('2D', '2D'),
        ('3D', '3D'),
        ('4DX', '4DX'),
        ('imax', 'IMAX'))
    place = models.CharField(blank=True, max_length=100)
    address = models.CharField(blank=True, max_length=100)
    session = models.CharField(max_length=4, choices=Session, default='2D')
    time_session = models.CharField(blank=True, max_length=100)
    price = models.IntegerField(blank=True, default=0)
    info_presen = models.ForeignKey(Presentation, on_delete=models.CASCADE, related_name="informations")

    def __str__(self):
        return self.place
