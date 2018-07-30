from . import views
from django.conf.urls import url

urlpatterns = [
  url(r'^movies/$', views.movie_list),
  url(r'^movies/(?P<pk>[0-9]+)$', views.movie_detail),
]