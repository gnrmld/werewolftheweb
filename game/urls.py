from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^game/create/$',  views.create, name='create'),
    url(r'^game/(?P<pk>\d+)',  views.board, name='board'),
    url(r'^game/$', views.game_list, name='game_list'),
    url(r'^game/end/(?P<pk>\d+)', views.end_game, name='end_game'),
]