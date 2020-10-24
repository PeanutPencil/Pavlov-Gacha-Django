from django.db import models
from users.models import User

class Card(models.Model):
    name = models.CharField(max_length=64)
    weapon = models.CharField(max_length=16)
    rarity = models.IntegerField()
    image = models.CharField(max_length=255)
    vrml_id = models.CharField(max_length=16)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="cards")