from django import forms
from django.forms import ModelForm
from .models import Work, Card, Activity


class DateInput(forms.DateInput):
    input_type = 'date'


class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['name', 'description', 'deadline', ]
        widgets = {
            'deadline': DateInput(),
        }
