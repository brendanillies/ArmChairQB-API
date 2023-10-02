from django.db import models
from django.db.models import CharField, IntegerField


class Teams(models.Model):
    class Meta:
        verbose_name_plural = "teams"
        db_table = "Teams"

    team_abbr = CharField(primary_key=True, max_length=4)
    team_name = CharField(max_length=25)
    team_id = IntegerField()
    team_nick = CharField(max_length=15)
    team_conf = CharField(max_length=3)
    team_division = CharField(max_length=10)
    team_color = CharField(max_length=7)
    team_color2 = CharField(max_length=7)
    team_color3 = CharField(max_length=7)
    team_color4 = CharField(max_length=7)
    team_logo_wikipedia = CharField(max_length=255)
    team_logo_espn = CharField(max_length=255)
    team_wordmark = CharField(max_length=255)
    team_conference_logo = CharField(max_length=255)
    team_league_logo = CharField(max_length=255)
    team_logo_squared = CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.team_name} ({self.team_abbr})"
