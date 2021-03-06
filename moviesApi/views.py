from django.shortcuts import render
from rest_framework import status, viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

from .models import Comment, Movie
from .serializers import CommentSerializer, MovieSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def movie_list(request, format=None):
  if request.method == 'GET':
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    search_result = {}
    if 'title' in request.data:
      searchTitle = request.data['title']
      url = 'http://www.omdbapi.com/?t=%s&apikey=6f78256' % searchTitle.replace(' ', '+')
      response = requests.get(url)
      search_was_successful = (response.status_code == 200)  # 200 = SUCCESS
      if search_was_successful:
        search_result = response.json()
        if 'Title' in search_result:
          movie = Movie.objects.create(title=search_result['Title'], year=search_result['Year'], plot=search_result['Plot']) 
          return Response(search_result, status=status.HTTP_201_CREATED)
        else:
          return Response(status=status.HTTP_404_NOT_FOUND)
      else:
        return Response(status=status.HTTP_404_NOT_FOUND)

  return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MovieSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentView(generics.ListCreateAPIView):
  serializer_class = CommentSerializer

  def get_queryset(self):
    queryset = Comment.objects.all()
    movie = self.request.query_params.get('movie', None)
    if movie is not None:
        queryset = queryset.filter(movie=movie)
    return queryset