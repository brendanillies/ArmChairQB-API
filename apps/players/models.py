from django.db import models
from django.db.models import (
    CharField,
    IntegerField,
    CASCADE,
    RESTRICT,
    ForeignKey,
    OneToOneField,
    FloatField,
)
import pandas as pd


class PlayerIdentifier(models.Model):
    class Meta:
        verbose_name_plural = "Identifiers"
        db_table = "PlayerIdentifiers"

    gsis_id = CharField(max_length=12, primary_key=True, db_column="player_id", verbose_name="player")

    espn_id = IntegerField(unique=True, name="espn")
    yahoo_id = IntegerField(unique=True, name="yahoo")
    name = CharField(max_length=50)
    db_season = IntegerField(null=True)

    def __str__(self) -> str:
        return f"""{self.name}
                (APP_ID: {self.gsis_id},
                YAHOO_ID: {self.yahoo_id})"""


class Player(models.Model):
    """
    Player model populated using the PlayerIdentifier & Roster (for headshot) models
    """

    class Meta:
        verbose_name_plural = "Players"
        db_table = "Players"

    player = OneToOneField(
        PlayerIdentifier, on_delete=RESTRICT, related_name="player"
    )
    headshot_url = CharField(max_length=255)
    age = FloatField()

    def __str__(self) -> str:
        return f"{self.player.name}"


class Roster(models.Model):
    class Meta:
        verbose_name_plural = "Rosters"
        db_table = "Rosters"

    season = IntegerField()
    team = ForeignKey("teams.Teams", on_delete=RESTRICT, related_name="team_roster")
    position = CharField(max_length=4)
    status = CharField(max_length=5)
    player_name = CharField(max_length=50)
    week = IntegerField()
    game_type = CharField(max_length=5)
    college = CharField(max_length=30)

    player_id = ForeignKey(
        PlayerIdentifier, on_delete=RESTRICT, related_name="player_roster"
    )


class DepthChart(models.Model):
    class Meta:
        verbose_name_plural = "Depth Charts"
        db_table = "DepthCharts"

    season = IntegerField()
    club_code = ForeignKey("teams.Teams", on_delete=RESTRICT, related_name="team_depth", db_column="team", verbose_name="team")
    week = IntegerField()
    game_type = CharField(max_length=5)
    depth_team = IntegerField()
    formation = CharField(max_length=15)
    gsis_id = ForeignKey(
        PlayerIdentifier, on_delete=RESTRICT, related_name="player_depth"
    )
    jersey_number = IntegerField()
    position = CharField(max_length=4)
    elias_id = CharField(max_length=10)
    depth_position = CharField(max_length=4, blank=True)
    full_name = CharField(max_length=50)

    def __str__(self) -> str:
        return f"""
            {self.full_name} ({self.club_code}) -
            Week: {self.week} ({self.game_type}),
            Depth: {self.depth_team},
            Position: {self.position} ({self.depth_position})
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
