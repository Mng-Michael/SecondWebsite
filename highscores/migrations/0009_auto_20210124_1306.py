# Generated by Django 3.1.5 on 2021-01-24 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('highscores', '0008_score_game_settings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='game_settings',
            new_name='decrypted_code',
        ),
        migrations.AddField(
            model_name='score',
            name='client_version',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='robot_position',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='time_of_score',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
