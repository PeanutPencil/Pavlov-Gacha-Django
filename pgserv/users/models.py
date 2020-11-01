from django.db import models

# Create your models here.
class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    rolls = models.IntegerField()
    claims = models.IntegerField()
    