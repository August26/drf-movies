from django.forms import ModelChoiceField
from rest_framework import serializers
from .models import Movie, City, Film, Info, Presentation


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('city', 'id', 'title', 'id_film', 'place', 'address', 'session', 'time_session', 'data_session',
                  'price', 'photo')
        depth = 3


class CitiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id', 'city', 'cookie', 'films')


class FilmsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = ('id', 'title', 'id_film', 'photo', 'city_film', 'presentations')


class PresentationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Presentation
        fields = ('id', 'data_session', 'film_presentations', 'informations')


class InfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Info
        fields = ('place', 'address', 'session', 'time_session', 'price', 'info_presen')
