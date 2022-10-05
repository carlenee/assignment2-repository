from django import forms

from .models import *

class TaskForm(forms.ModelForm):
    title= forms.CharField(widget= forms.TextInput())
    description= forms.CharField(widget=forms.Textarea(attrs={'style': 'width: 15em;'}))

    class Meta:
        model = Task
        fields = ('title', 'description')