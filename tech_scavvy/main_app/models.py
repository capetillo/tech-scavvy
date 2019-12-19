from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=100)
  #user = models.ForeignKey(User, on_delete=models.CASCADE)
  team = models.IntegerField()

  def __str__(self):
    return f"{self.name} on team {self.team}"