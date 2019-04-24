from .models import WorkList, Card
from django.forms.models import inlineformset_factory

CardInlineFormSet = inlineformset_factory(
                        WorkList, Card,
                        fields=['name', 'description', 'deadline_date'])
