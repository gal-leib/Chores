from django.db import models

class Chore(models.Model):
    title = models.CharField(max_length=200)
    reward = models.IntegerField()
