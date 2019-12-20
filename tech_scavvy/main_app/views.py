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
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')


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
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# creates a player
class PlayerCreate(LoginRequiredMixin, CreateView):
    model = Player
    fields = ['name', 'leader', 'team']

@login_required
def team_detail(request,team_id):
  #this is your team
  team = Team.objects.get(id=team_id)
  #these are all your team members
  teamMembers = Player.object.filter(team=team_id)
  #this is your match
  match = Match.object.filter(id=team.match)
  #these are the tasks in your match
  tasks = Task.object.filter(match=team.match)
  