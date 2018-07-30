from django.db import models
from django.utils import timezone

class Movie(models.Model):
  title = models.CharField(max_length=200)
  year = models.IntegerField()
  plot = models.TextField()

  def __str__(self):
    return self.title

class Comment(models.Model):
  movie = models.ForeignKey('moviesApi.Movie', on_delete=models.CASCADE, related_name='comments')
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.text