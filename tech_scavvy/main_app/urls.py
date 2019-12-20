from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('players/', views.players_index, name='index'),
    path('player/create/', views.PlayerCreate.as_view(), name='players_create'),
    path('team/create/', views.TeamCreate.as_view(), name='teams_create'),
    path('teams/<int:team_id>/', views.teams_detail, name='detail'),
    path('team/<int:team_id>/assoc_player/<int:player_id>/', views.assoc_player, name='assoc_player'),
    path('accounts/signup/', views.signup, name='signup'),
]
