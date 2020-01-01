from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
  class Meta:
    model = Task
    
    fields = ['task']


# class TaskCompleteForm(ModelForm):
#   class Meta:
#     model = Task
#     fields = ['team_1_complete', 'team_2_complete']
