from django.db import models
from datetime import datetime

class Chore(models.Model):
    title = models.CharField(max_length=200)
    reward = models.IntegerField()

class CompletedChore(models.Model):
    chore = models.ForeignKey(Chore)
    date_completed = Models.DateTimeField(default=datetime.now)
    player = models.ForeignKey('Player')
