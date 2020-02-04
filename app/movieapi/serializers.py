from django.forms import ModelChoiceField
from rest_framework import serializers
from .models import Movie, Cities, Films, Info, Presentation


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('city', 'id', 'title', 'id_film', 'place', 'address', 'session', 'time_session', 'data_session',
                  'price', 'photo')
        depth = 3


class CitiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cities
        fields = ('city', )
        depth = 3


class FilmsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Films
        fields = ('title', 'id_film', 'photo', 'city_films')
        depth = 3


class PresentationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Presentation
        fields = ('data_session', 'film_presentation')
        depth = 3


class InfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Info
        fields = ('place', 'address', 'session', 'time_session', 'price', 'presentation_info')
        depth = 3
