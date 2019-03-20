from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from django.contrib.auth.models import User


class Classes(models.Model):
    class_name = models.CharField(max_length=15)
    hit_die = models.PositiveSmallIntegerField()
    skill_points = models.PositiveSmallIntegerField()
    class_skills = ArrayField(models.CharField(max_length=32))
    alignments = ArrayField(models.CharField(max_length=16))
    armor_proficiencies = ArrayField(models.CharField(max_length=16))
    weapon_proficiencies = ArrayField(models.CharField(max_length=16))
    spell_caster = models.BooleanField()

class ClassLevels(models.Model):
    class_type = models.ForeignKey(Classes, on_delete=models.PROTECT)
    level = models.PositiveSmallIntegerField()
    level_info = JSONField()


class Races(models.Model):
    race_type = models.CharField(max_length=15)
    favored_class = models.ForeignKey(Classes, on_delete=models.PROTECT)
    size = models.CharField(max_length=10)
    speed = models.PositiveSmallIntegerField()
    race_info = JSONField()
    feats = ArrayField(models.CharField(max_length=64))
    languages = ArrayField(models.CharField(max_length=16))
    traits = ArrayField(models.CharField(max_length=64))
    special_abilities = ArrayField(models.CharField(max_length=64))
    ability_modifier = JSONField()


class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character_class = models.ForeignKey(Classes, on_delete=models.CASCADE)
    character_race = models.ForeignKey(Races, on_delete=models.CASCADE)
    name = models.CharField(max_length=48)
    level = models.PositiveSmallIntegerField()
    character_info = JSONField()
