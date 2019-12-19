from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Player(models.Model):
  name = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  team = models.ForeignKey(Team, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.name} on team {self.team}"
  
class Team(model.Model):
  team_name = models.CharField(max_length=100)
  winner = models.BooleanField()

  def __str__(self):
    return f"{self.name}"

  