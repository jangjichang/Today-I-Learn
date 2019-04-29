from django import forms
from django.forms import ModelForm
from .models import WorkList, Card, Activity
from django.forms.models import inlineformset_factory

class DateInput(forms.DateInput):
    input_type = 'date'


class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['name', 'description', 'deadline_date']
        widgets = {
            'deadline_date': DateInput(),
        }


