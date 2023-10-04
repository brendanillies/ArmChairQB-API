from django.db import models
from django.db.models import (
    CharField,
    IntegerField,
    DateField,
    TimeField,
    ForeignKey,
    RESTRICT,
)


class Stadium(models.Model):
    class Meta:
        db_table = "Stadiums"

    stadium_id = CharField(max_length=7, primary_key=True, editable=False)
    stadium = CharField(max_length=70, default="", name="name", verbose_name="name")

    def __str__(self) -> str:
        return f"{self.name} ({self.stadium_id})"


class Schedule(models.Model):
    class Meta:
        verbose_name_plural = "Schedule"
        db_table = "Schedules"

    game_id = models.CharField(primary_key=True, max_length=20)
    season = IntegerField(editable=False)
    game_type = CharField(editable=False, max_length=4)
    week = IntegerField(editable=False)
    gameday = DateField(editable=False)
    weekday = CharField(editable=False, max_length=9)
    gametime = TimeField(editable=False)
    away_team = ForeignKey(
        "teams.Teams", on_delete=RESTRICT, related_name="schedule_away", editable=False
    )
    home_team = ForeignKey(
        "teams.Teams", on_delete=RESTRICT, related_name="schedule_home", editable=False
    )
    location = CharField(editable=False, max_length=4)
    overtime = IntegerField(editable=False, default=0)
    espn = IntegerField(
        editable=False,
        name="espn_game_id",
        verbose_name="espn_game_id",
        db_column="espn_game_id",
    )
    div_game = IntegerField(
        editable=False, verbose_name="divisional_game", db_column="divisional_game"
    )
    stadium_id = ForeignKey(Stadium, on_delete=RESTRICT, editable=False)
    surface = CharField(max_length=10, default="")
    roof = CharField(max_length=8, default="")

    def __str__(self) -> str:
        return f"{self.season} Week {self.week} - {self.away_team} vs. {self.home_team}"


class PlayByPlay(models.Model):
    class Meta:
        verbose_name_plural = "PlayByPlay"
        db_table = "PlayByPlay"
