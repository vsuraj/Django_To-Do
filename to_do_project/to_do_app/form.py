from audioop import add
from django import forms
from .models import task

class task_form(forms.ModelForm):
    class Meta:
        model = task
        fields = ('task_title', 'task_discription', 'task_status')