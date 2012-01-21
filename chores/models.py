from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Chore(models.Model):
    title = models.CharField(max_length=200)
    reward = models.IntegerField()

class CompletedChore(models.Model):
    chore = models.ForeignKey(Chore)
    date_completed = Models.DateTimeField(default=datetime.now)
    player = models.ForeignKey('Player')

class Player(models.Model):
    user = models.OneToOneField(User)
    points = models.IntegerField()

def create_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)

post_save.connect(create_player, sender=User)
