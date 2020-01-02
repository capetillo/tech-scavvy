from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskForm
import uuid
import boto3
from .models import Player, Team, Match, Task, Photo


S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'techscavvy'


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


@login_required
def add_task(request, match_id):
    # create the ModelForm using the data in request.POST
    form = TaskForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the match_id assigned
        new_task = form.save(commit=False)
        new_task.match_id = match_id
        new_task.save()
    return redirect('detail', match_id=match_id)


class TaskList(LoginRequiredMixin, ListView):
    model = Task


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task


class MatchCreate(CreateView):
    model = Match
    fields = ['name']
# saves associated model if form is valid

    def form_valid(self, form):
        form.instance.judge = self.request.user
        return super().form_valid(form)


@login_required
def match_index(request, match_id):
    match = Match.objects.filter(id=match_id)
    return render(request, 'match/index.html', {'match': match})


@login_required
def match_detail(request, match_id):
    #match = Match.objects.all()
    match = Match.objects.get(id=match_id)
    task_form = TaskForm()
    return render(request, 'match/detail.html', {'match': match, 'task_form': task_form, })

def task_complete(request, match_id):
    match= Match.objects.get(id=match_id)
    task_complete_form = TaskCompleteForm()
    return render(request,'match/index.html', {'match': match, 'task_complete_form': task_complete_form, })
# creates a player


class PlayerCreate(CreateView):
    model = Player
    fields = ['name', 'team', 'leader']
# saves associated model if form is valid

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required
def players_index(request):
    players = Player.objects.filter(user=request.user)
    return render(request, 'players/index.html', {'players': players})


@login_required
def players_detail(request, player_id, team_id):
    player = Player.objects.get(id=player_id)
    team = Team.objects.get(id=player.team.id)
    opposite_team = Team.objects.exclude(id=player.team.id)

    return render(request, 'players/index.html', {
        'player': player,
        'opposite_team': opposite_team

    })

@login_required
def teams_create(request,player_id):
    player = Player.objects.get(id=player_id)
    
    return render(request, 'teams/create.html', {'player': player})

def teams_index(request):
    teams = Team.objects.all()
    players = Player.objects.all()
    return render(request, 'teams/index.html', {'teams': teams, 'players': players})


@login_required
def assoc_team(request, player_id, team_id):
    player = Player.objects.get(id=player_id)
    player.teams.add(team_id)
    return redirect()


@login_required
def team_detail(request, team_id):
    team = Team.objects.get(id=team_id)
    match = Match.objects.get(id=team.match)
    tasks = Task.objects.get(match=match.id)
    photos = Photo.objects.get(team=team_id)

    # this removes all the whoAndWhat that aren't related to the team
    tasks = tasks.whoAndWhat.filter(team=team.id)

    # this sorts the tasks by the order of tasks from the biggest (being the last)
    # to the smallest being the first
    tasks = tasks.sort(key=lambda x: x.task_number, reverse=True)

    return redirect(request, 'teams/detail.html', {'team': team, 'match': match, 'tasks': tasks, 'photos': photos})


def add_photo(request, task_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:

            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string

            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            print(url)
            print(task_id)
            photo = Photo(url=url, task_id=task_id)
            print(photo.url)
            photo.save()

        except:
            print('An error occurred uploading file to S3')
    return redirect('task_detail', pk=task_id)
