from . import views
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('comments', views.CommentView)

urlpatterns = [
  url(r'^movies/$', views.movie_list, name='movie_list'),
  url(r'^movies/(?P<pk>[0-9]+)$', views.movie_detail, name='movie_detail'),
  path('', include(router.urls))
]

urlpatterns += router.urls