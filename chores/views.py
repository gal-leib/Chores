from django.shortcuts import render, redirect
from chores.models import Player, Chore, CompletedChore
from chores.forms import CompleteChoreForm
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse

def home(request):
    recently_completed = CompletedChore.objects.all().order_by('-date_completed')[:5]
    #todo sum all the points so we could use a progress bar
    return render(request, 'home.html', {'players' : Player.objects.all(),
        'recently_completed' : recently_completed, 'form' : CompleteChoreForm()})

class CompleteChoreView(CreateView):
    form_class = CompleteChoreForm

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.player = self.request.user.get_profile()
        self.object.player.add_points(self.object.chore.reward)
        self.object.player.save()
        self.object.save()
        return redirect('home')

