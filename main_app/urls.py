from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('players/', views.players_index, name='index'),
    path('players/create/', views.PlayerCreate.as_view(), name='players_create'),
    path('players/<int:player_id>/', views.players_detail, name='detail'),
    path('players/<int:player_id>/assoc_team/<int:team_id>/', views.assoc_team, name='assoc_team'),
    
    path('teams/', views.teams_index, name='teams_index'),
    path('teams/<int:team_id>',views.team_detail, name='teams_detail'),
    path('teams/create/', views.TeamCreate.as_view(), name='teams_create'),
    
    path('match/create/', views.MatchCreate.as_view(), name='match_create'),
    path('match/<int:match_id>/', views.match_detail, name='detail'),
    
    
    path('accounts/signup/', views.signup, name='signup'),
]
