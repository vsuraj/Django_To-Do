from django import forms
from app.models import add_task

class task(forms.ModelForm):
    class Meta:
        model = add_task
        fields = ('title', 'discription', 'status')