import json
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from django.urls import reverse
from .models import Comment, Movie
from .serializers import CommentSerializer, MovieSerializer

client = APIClient()

class ShouldGetAllMoviesTest(TestCase):

  def setUp(self):
    Movie.objects.create(
        title='Lion King', 
        plot='Story of Simba', 
        year=1994)
    Movie.objects.create(
        title='Reservoir Dogs', 
        plot='After a simple jewelry heist goes terribly wrong, the surviving criminals begin to suspect that one of them is a police informant.', 
        year=1992)
    Movie.objects.create(
        title='Batman', 
        plot='The Dark Knight of Gotham City begins his war on crime with his first major enemy being the clownishly homicidal Joker.', 
        year=1989)

  def test_get_all_movies(self):
    # get API response
    response = client.get(reverse('movie_list'))
    # get data from db
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    self.assertEqual(response.data, serializer.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

class ShouldPostMovie(TestCase):

  def setUp(self):
    self.movie_data = {'title': 'Batman'}
    self.response = client.post(
      reverse('movie_list'),
      self.movie_data,
      format="json"
    )

  def test_post_movie(self):
    self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

class ShouldNotPostMovie_whenTitleNotGiven(TestCase):

  def setUp(self):
    self.movie_data = {"title": "ThereIsNoMovieWithNameLikeThat123123"}
    self.response = client.post(
      reverse('movie_list'),
      self.movie_data,
      format="json"
    )

  def test_post_movie(self):
    self.assertEqual(self.response.status_code, status.HTTP_404_NOT_FOUND)  

class ShouldPostComments(TestCase):

  def setUp(self):
    movie_one = Movie.objects.create(
        title='Lion King', 
        plot='Story of Simba', 
        year=1994)
    movie_two = Movie.objects.create(
        title='Reservoir Dogs', 
        plot='After a simple jewelry heist goes terribly wrong, the surviving criminals begin to suspect that one of them is a police informant.', 
        year=1992)
    movie_three = Movie.objects.create(
        title='Batman', 
        plot='The Dark Knight of Gotham City begins his war on crime with his first major enemy being the clownishly homicidal Joker.', 
        year=1989)
    Comment.objects.create(
        movie=movie_one,
        text='very good movie')
    Comment.objects.create(
        movie=movie_two,
        text='not so good')
    Comment.objects.create(
        movie=movie_two,
        text='what are you saying? its the best')

  def test_get_all_movies(self):
    # get API response
    response = client.get(reverse('comment_list'))
    # get data from db
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    self.assertEqual(response.data, serializer.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)



