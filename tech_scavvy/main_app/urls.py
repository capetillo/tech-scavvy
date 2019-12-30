from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('players/', views.players_index, name='index'),
    path('players/create/', views.PlayerCreate.as_view(), name='players_create'),
    # path('players/<int:player_id>/', views.available_teams, name='available_teams'),
    path('teams/', views.teams_index, name='teams_index'),
    path('teams/create/', views.TeamCreate.as_view(), name='teams_create'),
    path('leaders/', views.leaders_index, name='leaders_index'),
    path('teams/assoc_team/players/<int:player_id>/', views.assoc_team, name='assoc_team'),
    path('accounts/signup/', views.signup, name='signup'),
]
