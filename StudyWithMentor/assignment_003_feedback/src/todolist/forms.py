from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
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


CardInlineFormSet = inlineformset_factory(Work, Card, form=CardForm, extra=3)
