# Generated by Django 3.0.3 on 2020-03-22 15:48

from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(db_column='class', max_length=16, unique=True)),
                ('hit_die', models.PositiveSmallIntegerField()),
                ('skill_points', models.PositiveSmallIntegerField()),
                ('class_skills', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32), size=None)),
                ('alignments', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=16), size=None)),
                ('armor_proficiencies', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=16), size=None)),
                ('weapon_proficiencies', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=16), size=None)),
                ('spell_caster', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Races',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.CharField(max_length=16, unique=True)),
                ('favored_class', models.CharField(max_length=16)),
                ('size', models.CharField(max_length=10)),
                ('speed', models.PositiveSmallIntegerField()),
                ('race_info', django.contrib.postgres.fields.jsonb.JSONField()),
                ('feats', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), size=None)),
                ('languages', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=16), size=None)),
                ('traits', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), size=None)),
                ('special_abilities', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), size=None)),
                ('ability_modifier', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='ClassLevels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField()),
                ('level_info', django.contrib.postgres.fields.jsonb.JSONField()),
                ('class_name', models.ForeignKey(db_column='class', on_delete=django.db.models.deletion.PROTECT, to='creator.Classes')),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('level', models.PositiveSmallIntegerField()),
                ('character_info', django.contrib.postgres.fields.jsonb.JSONField()),
                ('character_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creator.Classes')),
                ('character_race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creator.Races')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
