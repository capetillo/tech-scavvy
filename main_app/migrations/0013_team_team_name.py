# Generated by Django 2.2.6 on 2020-01-02 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_remove_team_team_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]