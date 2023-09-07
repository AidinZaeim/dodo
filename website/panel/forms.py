from django import forms
from .models import Label, Task

class AddTask(forms.ModelForm):
    label_dict = tuple(Label.objects.all().value_list("name"))
    priority_choices = (
        ('a',  'important and urgent'),
        ('b', 'important but not urgent'),
        ('c', 'not important but urgent'),
        ('d', 'not important, not urgent'),
    )
    name = forms.CharField(max_length=255)
    label = forms.ChoiceField(choices=label_dict)
    priority = forms.ChoiceField(choices=priority_choices)
    undertaker = forms.CharField(max_length=255)
    description = forms.CharField(max_length=400)

    class Meta:
        model = Task
        fields = ["name", "label", "priority", "undertaker", "description"]

class AddSection(forms.ModelForm):
    name = forms.CharField(max_length=100)