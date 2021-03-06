# Generated by Django 3.0.3 on 2020-03-24 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('creator', '0002_auto_20200322_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characters',
            name='character_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='creator.Classes'),
        ),
        migrations.AlterField(
            model_name='characters',
            name='character_race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='creator.Races'),
        ),
        migrations.AlterField(
            model_name='characters',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='creator.ClassLevels'),
        ),
        migrations.AlterField(
            model_name='characters',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
