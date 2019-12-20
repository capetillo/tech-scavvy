from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # designates team leader.. can only be one per team
    leader = models.BooleanField()

    def __str__(self):
        return f"{self.name} on team {self.team}"


class Team(model.Model):
    team_name = models.CharField(max_length=100)
    winner = models.BooleanField()
    team_id = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


class Judge(model.Models):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Task(model.Models):
    task = models.CharField(max_length=100)

    #this allows each task that is needed in a given match to have the many to one with team 1 and team 2
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE)

    #this allows us to know the order of the tasks and programatically work on them in that order
    task_number = models.IntegerField(default=-1)

    #this will alert us to the completeness of the tasks or lack there of
    team1_complete = models.BooleanField(default='False')
    team2_complete = models.BooleanField(default='False')

    #TODO: add a function that resets the team1 and 2 keys and bools and task number to be reused next game