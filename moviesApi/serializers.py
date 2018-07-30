from rest_framework import serializers
from .models import Comment, Movie

class MovieSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = ('id', 'title', 'year', 'plot')

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ('id', 'movie', 'text', 'created_date')