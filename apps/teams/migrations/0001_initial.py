# Generated by Django 4.2.5 on 2023-10-02 13:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Teams",
            fields=[
                (
                    "team_abbr",
                    models.CharField(max_length=4, primary_key=True, serialize=False),
                ),
                ("team_name", models.CharField(max_length=25)),
                ("team_id", models.IntegerField()),
                ("team_nick", models.CharField(max_length=15)),
                ("team_conf", models.CharField(max_length=3)),
                ("team_division", models.CharField(max_length=10)),
                ("team_color", models.CharField(max_length=7)),
                ("team_color2", models.CharField(max_length=7)),
                ("team_color3", models.CharField(max_length=7)),
                ("team_color4", models.CharField(max_length=7)),
                ("team_logo_wikipedia", models.CharField(max_length=255)),
                ("team_logo_espn", models.CharField(max_length=255)),
                ("team_wordmark", models.CharField(max_length=255)),
                ("team_conference_logo", models.CharField(max_length=255)),
                ("team_league_logo", models.CharField(max_length=255)),
                ("team_logo_squared", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name_plural": "teams",
                "db_table": "Teams",
            },
        ),
    ]
