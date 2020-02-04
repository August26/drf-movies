from rest_framework import viewsets
from . import serializers
from rest_framework import filters
from .models import Movie, Cities, Films, Info, Presentation
import django_filters.rest_framework
from custom_permisions import IsAnonCreate


class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    permission_classes = (IsAnonCreate, )
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['title']  # ['place', 'address', 'session', 'time_session', 'price']
    search_fields = ['price']
    ordering_fields = ['price']


class CitiesView(viewsets.ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = serializers.CitiesSerializer
    permission_classes = (IsAnonCreate, )
    filter_backends = [filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter]


class FilmsView(viewsets.ModelViewSet):
    queryset = Films.objects.all()
    serializer_class = serializers.FilmsSerializer
    permission_classes = (IsAnonCreate,)
    filter_backends = [filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter]


class InfoView(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = serializers.InfoSerializer
    permission_classes = (IsAnonCreate, )
    filter_backends = [filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter]


class PresentationView(viewsets.ModelViewSet):
    queryset = Presentation.objects.all()
    serializer_class = serializers.PresentationSerializer
    permission_classes = (IsAnonCreate, )
    filter_backends = [filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter]
