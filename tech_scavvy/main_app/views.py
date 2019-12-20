from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Player, Team, Match, Task


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# creates a player
class PlayerCreate(LoginRequiredMixin, CreateView):
    model = Player
    fields = ['name', 'team', 'leader']
#saves associated model if form is valid
    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

@login_required
def players_index(request):
  players = Player.objects.filter(user=request.user)
  return render(request, 'players/index.html', { 'players': players })
    
class TeamCreate(LoginRequiredMixin, CreateView):
    model = Team
    fields = ['team_name', 'match']
    
@login_required
def assoc_player(request, team_id, player_id):
  team = Team.objects.get(id=team_id)
  team.players.add(player_id)
  return redirect(team)

