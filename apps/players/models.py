from django.db import models
from django.db.models import CharField, IntegerField, RESTRICT, ForeignKey, FloatField
import pandas as pd


class PlayerIdentifier(models.Model):
    class Meta:
        verbose_name_plural = "Player Identifiers"
        db_table = "PlayerIdentifiers"

    gsis_id = CharField(max_length=12, primary_key=True)
    espn_id = IntegerField(null=True)
    yahoo_id = IntegerField(null=True)
    name = CharField(
        max_length=50, name="player_name", db_column="player_name", default=""
    )
    college = CharField(max_length=30, null=True)
    headshot = CharField(max_length=255, default="")
    age = FloatField(null=True)

    db_season = IntegerField(null=True)

    def __str__(self) -> str:
        return f"""{self.name}
                (APP_ID: {self.gsis_id},
                YAHOO_ID: {self.yahoo_id})"""


class Roster(models.Model):
    class Meta:
        verbose_name_plural = "Rosters"
        db_table = "Rosters"

    gsis_id = ForeignKey(
        PlayerIdentifier, on_delete=RESTRICT, related_name="player_roster"
    )
    season = IntegerField()
    week = IntegerField()
    team = ForeignKey("teams.Teams", on_delete=RESTRICT, related_name="team_roster")
    status = CharField(max_length=5)

    def __str__(self) -> str:
        return (
            f"{self.gsis_id.player_roster.name} - {self.team}, Season {self.season}, Week {self.week}"
        )


class DepthChart(models.Model):
    class Meta:
        verbose_name_plural = "Depth Charts"
        db_table = "DepthCharts"

    gsis_id = ForeignKey(
        PlayerIdentifier, on_delete=RESTRICT, related_name="player_depth"
    )
    season = IntegerField()
    team = ForeignKey(
        "teams.Teams",
        on_delete=RESTRICT,
        related_name="team_depth",
    )
    week = IntegerField()
    depth = IntegerField()
    formation = CharField(max_length=15)
    position = CharField(max_length=4)
    depth_position = CharField(max_length=4, blank=True)

    def __str__(self) -> str:
        return f"""
            {self.gsis_id.name} ({self.team}) -
            Week: {self.week},
            Depth: {self.depth},
            Depth Position: {self.depth_position},
            Position: {self.position}
            """

    def save(self, *args, **kwargs):
        if (
            self.depth_position is None
            or self.depth_position == ""
            or pd.isna(self.depth_position)
        ):
            self.depth_position = self.position
            self.depth_team += 1

        super().save(*args, **kwargs)
