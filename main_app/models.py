from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.urls import reverse
import random

# Create your models here.


class Match(models.Model):
    name = models.CharField(max_length=100)
    judge = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'match_id': self.id})

    def __str__(self):
        return f"name is: {self.name} and judge is: {self.judge}"


class MatchAndWinner(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    winner = models.BooleanField(default='False')


class Team(models.Model):
    team_name = models.CharField(max_length=100)
    matchAndWinner = models.ForeignKey(
        MatchAndWinner, on_delete=models.CASCADE, default=None)
    ready = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.team_name}"

    def get_absolute_url(self):
        return reverse('teams_create')


class Player(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # designates team leader can only be one per team
    leader = models.BooleanField(default='False')

    def __str__(self):
        return f"{self.name} on team {self.team}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'player_id': self.id})


# this is to allow the task to have multiple teams attached to it and each of those teams is attached to the task
class whoAndWhat(models.Model):
    #this connects the task to the match (because I'm paranoid idk)
    match = models.ForeignKey(Match,on_delete=models.CASCADE)
    # this is the team for this object in the task
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # this allows us to know the order of the tasks and programatically work on them in that order
    task_number = models.IntegerField(default=-1)
    #this doesn't need to be set in the create method
    complete = models.BooleanField(default=False)
    


class Task(models.Model):
    task = models.CharField(max_length=250, unique=True)
    whoAndWhat = models.ManyToManyField(whoAndWhat)


class Photo(models.Model):
    url = models.CharField(max_length=200)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    # team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for task_id: {self.task_id} @{self.url}"


def make_match(team_id):
    team1 = Team.objects.filter(id=team_id)

    #just in case the team1 leader clicked ready already and is impatience
    #this will insure that they don't end up in the list of readys if they
    #get matched with another team or prevent them from matching with themselves
    team1.ready=False

    readyTeams = Team.objects.filter(ready=True)

    #if there are any other teams that are ready
    if readyTeams:
        team2 = readyTeams[0]
        team2.ready = False

        # create the match
        match = Match(Name=team1.name+team2.name)
        match.save()
        # create match and winner for each team
        # pull 5 random tasks
        randomIndecies = []
        tasks = Task.objects.all()
        #this just makes 5 random numbers from the size of the tasks arr
        #or if there are less than 5 tasks in existence than just make 
        #it all of those
        try:
            randomIndecies = random.sample(range(0, len(tasks)-1), 5)
        except ValueError:
            randomIndecies = range(0,len(tasks)-1)
        taskNum=0
        for num in randomIndecies:
            # create who and whats for each task for each team and set their task order
            tasks[num].whoAndWhat.create(match = match,team = team1,task_number = taskNum)
            tasks[num].whoAndWhat.create(match = match,team = team2,task_number = taskNum)
            taskNum+=1
            tasks[num].save()
    else:
        #otherwise put the team in the ready queue
        team1.ready = True