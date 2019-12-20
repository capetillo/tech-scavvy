from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('player/create/', views.PlayerCreate.as_view(), name='players_create')
    # signup path
    #path('accounts/signup/', views.signup, name='signup'),
]
