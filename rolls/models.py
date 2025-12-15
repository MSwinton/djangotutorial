from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=30)

class CharStat(models.Model):
    character_id = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    value = models.PositiveSmallIntegerField(default=0)