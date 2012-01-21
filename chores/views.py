from django.shortcuts import render
from chores.models import Player, Chore, CompletedChore

def home(request):
    recently_completed = CompletedChore.objects.all().order_by('-date_completed')[:5]
    return render(request, 'home.html', {'players' : Player.objects.all(),
        'recently_completed' : recently_completed})
