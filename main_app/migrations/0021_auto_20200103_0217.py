# Generated by Django 3.0.2 on 2020-01-03 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_auto_20200103_0128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='whoAndWhat',
        ),
        migrations.AddField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
