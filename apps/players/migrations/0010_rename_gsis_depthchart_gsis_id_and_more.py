# Generated by Django 4.2.5 on 2023-10-07 13:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("players", "0009_rename_club_code_depthchart_team"),
    ]

    operations = [
        migrations.RenameField(
            model_name="depthchart",
            old_name="gsis",
            new_name="gsis_id",
        ),
        migrations.RenameField(
            model_name="roster",
            old_name="gsis",
            new_name="gsis_id",
        ),
        migrations.RemoveField(
            model_name="depthchart",
            name="game_type",
        ),
        migrations.RemoveField(
            model_name="roster",
            name="game_type",
        ),
        migrations.AlterField(
            model_name="playeridentifier",
            name="gsis_id",
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
    ]
