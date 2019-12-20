from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Team(models.Model):
  team_name = models.CharField(max_length=100)
  winner = models.BooleanField()
  team_id = models.IntegerField()

  def __str__(self):
    return f"{self.name}"

  def get_absolute_url(self):
    return reverse('detail', kwargs={'team_id': self.id})

class Match(models.Model):
  name = models.CharField(max_length=100)
  judge = models.ForeignKey(User, on_delete=models.CASCADE)

class Team(models.Model):
  team_name = models.CharField(max_length=100)
  winner = models.BooleanField()
  team_id = models.IntegerField()

    #this tells the team what match they are in
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    def __str__(self):
      return f"{self.team_name}"

class Player(models.Model):
  name = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # designates team leader.. can only be one per team
  leader = models.BooleanField(default='False')

  def __str__(self):
    return f"{self.name} on team {self.team}"

class Task(models.Model):
    task = models.CharField(max_length=100)
    team1_complete = models.BooleanField(default='False')
    team2_complete = models.BooleanField(default='False')
    match = models.ForeignKey(Match, on_delete = models.CASCADE )

    # this allows us to know the order of the tasks and programatically work on them in that order
  task_number = models.IntegerField(default=-1)

  def new_game_reset(self):
    self.team1_complete = 'False'
    self.team2_complete = 'False'
    self.task_number = -1
