# Generated by Django 2.2.6 on 2020-01-01 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_team_team_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='matchAndWinner',
        ),
    ]