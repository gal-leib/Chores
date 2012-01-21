from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Chore(models.Model):
    title = models.CharField(max_length=200)
    reward = models.IntegerField()

    def __unicode__(self):
        return u'{0} - {1} points'.format(self.title, self.reward)

class CompletedChore(models.Model):
    chore = models.ForeignKey(Chore)
    date_completed = models.DateTimeField(default=datetime.now)
    player = models.ForeignKey('Player')

    def __unicode__(self):
        return u'{0} by {1} at {2}'.format(self.chore.title, self.player.user.username, self.date_completed)

class Player(models.Model):
    user = models.OneToOneField(User)
    points = models.IntegerField()

    def __unicode__(self):
        return u'{0} : {1} points'.format(self.user.username, self.points)

def create_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)

post_save.connect(create_player, sender=User)
