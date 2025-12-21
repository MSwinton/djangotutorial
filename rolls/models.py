from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=50)
    attr_dex = models.PositiveSmallIntegerField(default=1)
    attr_stam = models.PositiveSmallIntegerField(default=1)
    attr_str = models.PositiveSmallIntegerField(default=1)
    attr_app = models.PositiveSmallIntegerField(default=1)
    attr_cha = models.PositiveSmallIntegerField(default=1)
    attr_manip = models.PositiveSmallIntegerField(default=1)
    attr_per = models.PositiveSmallIntegerField(default=1)
    attr_int = models.PositiveSmallIntegerField(default=1)
    attr_wits = models.PositiveSmallIntegerField(default=1)

class Ability(models.Model):
    character_id = models.ForeignKey(Character, on_delete=models.CASCADE)
    ability = models.CharField(max_length=20)
    value = models.PositiveSmallIntegerField(default=0)
    caste_or_favored = models.BooleanField(default=0)

class Intimacy(models.Model):
    character_id = models.ForeignKey(Character, on_delete=models.CASCADE)
    intimacy = models.TextField(max_length=200)

class Specialty(models.Model):
    ability_id = models.ForeignKey(Ability, on_delete=models.CASCADE)
    specialty = models.TextField(max_length=20)
