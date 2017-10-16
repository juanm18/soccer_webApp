from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$',index),
    url(r'^leagues/(?P<id>\d+)$',leagues),
    url(r'^teams/(?P<id>\d+)$',teams),
    url(r'^leagues/champions_league/(?P<id>\d+)$', champions)
]
