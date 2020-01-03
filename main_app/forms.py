from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
  class Meta:
    model = Task
    
    fields = ['task','task_number']


class TaskCompleteForm(ModelForm):
  class Meta:
    model = Task

    fields = ['complete']