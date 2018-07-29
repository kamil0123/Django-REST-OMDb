from django.db import models

class Movie(models.Model):
  title = models.CharField(max_length=200)
  year = models.IntegerField()
  plot = models.TextField()

  def __str__(self):
    return self.title

