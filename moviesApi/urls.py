from . import views
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
  url(r'^movies/$', views.movie_list, name='movie_list'),
  url(r'^movies/(?P<pk>[0-9]+)$', views.movie_detail, name='movie_detail'),
  url(r'^comments/$', views.CommentView.as_view(), name='comment_list'),
  path('', include(router.urls))
]

urlpatterns += router.urls