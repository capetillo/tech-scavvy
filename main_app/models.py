from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.urls import reverse
import random

# Create your models here.

class Match(models.Model):
    name = models.CharField(max_length=100,default=None)
    judge = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('match_detail')

    def __str__(self):
        return f"name is: {self.name} and judge is: {self.judge}"


CHOICES = [(i, i) for i in range(3)]


class Team(models.Model):
    team_name = models.CharField(max_length=100,default=None)
    ready = models.BooleanField(default=False)
    #team_number = models.IntegerField(choices=CHOICES)

    def __str__(self):
        return f"{self.team_name}"

    def get_absolute_url(self):
        return reverse('teams_detail',kwargs={'pk': self.id})


class Player(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.CASCADE)
    # designates team leader can only be one per team
    leader = models.BooleanField(default='False')

    def __str__(self):
        return f"{self.name} on team {self.team}"

    def get_absolute_url(self):
        return reverse('teams_index')

complete = [(True, False)]

# this is to allow the task to have multiple teams attached to it and each of those teams is attached to the task
class WhoAndWhat(models.Model):
    # this is the team for this object in the task
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False, choices=complete)

class Task(models.Model):
    task = models.CharField(max_length=250, unique=True)
    team = models.ManyToManyField(Team)
    # whoAndWhat = models.ManyToManyField(WhoAndWhat,blank=True)
    task_number = models.IntegerField(default=0)
    complete = models.BooleanField(default=False)
    # def get_absolute_url(self):
    #     return reverse('task_detail', kwargs={'pk':self.id ,'team_id': self.team_id})


class Photo(models.Model):
    url = models.CharField(max_length=200)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    # team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for task_id: {self.task_id} @{self.url}"
