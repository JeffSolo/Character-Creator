from django.contrib.postgres.fields import JSONField, ArrayField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Classes(models.Model):
    class_name = models.CharField(db_column='class', unique=True, max_length=16)
    hit_die = models.PositiveSmallIntegerField()
    skill_points = models.PositiveSmallIntegerField()
    class_skills = ArrayField(models.CharField(max_length=32))
    alignments = ArrayField(models.CharField(max_length=16))
    armor_proficiencies = ArrayField(models.CharField(max_length=16))
    weapon_proficiencies = ArrayField(models.CharField(max_length=16))
    spell_caster = models.BooleanField()


class Levels(models.Model):
    level = models.PositiveSmallIntegerField()
    class_name = models.ForeignKey(Classes, to_field='class_name', db_column='class', on_delete=models.PROTECT)
    level_info = JSONField()


class Races(models.Model):
    race = models.CharField(unique=True, max_length=16)
    # TODO: can't be foreign key since Human='All', how to handle?
    #favored_class = models.ForeignKey(Classes, to_field='class_name', on_delete=models.PROTECT)
    favored_class = models.CharField(max_length=16)
    size = models.CharField(max_length=10)
    speed = models.PositiveSmallIntegerField()
    race_info = JSONField()
    feats = ArrayField(models.CharField(max_length=64))
    languages = ArrayField(models.CharField(max_length=16))
    traits = ArrayField(models.CharField(max_length=64))
    special_abilities = ArrayField(models.CharField(max_length=64))
    ability_modifier = JSONField()


class Characters(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=48)
    character_class = models.ForeignKey(Classes, to_field='class_name', on_delete=models.PROTECT)
    character_race = models.ForeignKey(Races, to_field='race', on_delete=models.PROTECT)
    level = models.ForeignKey(Levels, on_delete=models.PROTECT)
    character_info = JSONField()
