from .models import Movie
from .serializers import MovieSerializer
from rest_framework import viewsets
from rest_framework import generics
from . import serializers


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

