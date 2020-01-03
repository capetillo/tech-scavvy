from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('players/', views.players_index, name='index'),
    path('players/create/', views.PlayerCreate.as_view(), name='players_create'),
    path('players/<int:player_id>',views.players_detail, name='detail'),
    path('players/<int:player_id>/assoc_team/<int:team_id>/',views.assoc_team, name='assoc_team'),

    path('teams/', views.TeamList.as_view(), name='teams_index'),
    path('teams/<int:pk>/', views.TeamDetail.as_view(), name='teams_detail'),
    path('teams/create/', views.TeamCreate.as_view(), name='teams_create'),
    path('teams/<int:pk>/update/', views.TeamUpdate.as_view(), name='teams_update'),
    path('teams/<int:pk>/delete/', views.TeamDelete.as_view(), name='teams_delete'),
    path('teams/<int:pk>/assoc_team/<int:player_id>/',views.assoc_team, name='assoc_team'),

    path('match/create/', views.MatchCreate.as_view(), name='match_create'),
    path('match/<int:match_id>/', views.match_detail, name='match_detail'),
    path('match/', views.match_index, name='index'),
    path('match/<int:match_id>/add_task/', views.add_task, name='add_task'),

    path('tasks/', views.TaskList.as_view(), name='task_index'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete'),
    path('accounts/signup/', views.signup, name='signup'),


    path('tasks/<int:task_id>/add_photo/', views.add_photo, name='add_photo'),
]
