from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Match(models.Model):
  name = models.CharField(max_length=100)
  judge = models.ForeignKey(User, on_delete=models.CASCADE)

class Team(models.Model):
  team_name = models.CharField(max_length=20, default=None)
  winner = models.BooleanField(default='False')
  # this tells the team what match they are in
  # match = models.ForeignKey(Match, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.team_name}"

  def get_absolute_url(self):
    return reverse('assoc_team')

class Player(models.Model):
  name = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.CASCADE)
  # designates team leader.. can only be one per team
  leader = models.BooleanField(default='False')

  def __str__(self):
    return f"{self.name} on team {self.team}"

  def get_absolute_url(self):
    return reverse('teams_index')

class Task(models.Model):
  task = models.CharField(max_length=100)
  team1_complete = models.BooleanField(default='False')
  team2_complete = models.BooleanField(default='False')
  match = models.ForeignKey(Match, on_delete=models.CASCADE)
    # this allows us to know the order of the tasks and programatically work on them in that order
  task_number = models.IntegerField(default=-1)

  def new_game_reset(self):
    self.team1_complete = 'False'
    self.team2_complete = 'False'
    self.task_number = -1
