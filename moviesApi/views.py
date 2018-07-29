from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer

# Create your views here.
class MovieView(viewsets.ModelViewSet):
  queryset = Movie.objects.all()
  serializer_class = MovieSerializer
