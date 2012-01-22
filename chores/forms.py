from django.forms import ModelForm
from chores.models import CompletedChore

class CompleteChoreForm(ModelForm):
    class Meta:
        model = CompletedChore
        exclude = ('player',)

