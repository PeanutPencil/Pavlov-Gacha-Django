from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=64)
    weapon = models.CharField(max_length=16)
    rarity = models.IntegerField()