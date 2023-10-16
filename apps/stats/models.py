from django.db import models
from django.db.models import IntegerField, RESTRICT, ForeignKey, FloatField


class PlayerStats(models.Model):
    class Meta:
        verbose_name_plural = "Player Stats"
        db_table = "PlayerStats"

    gsis_id = ForeignKey(
        "players.PlayerIdentifier",
        on_delete=RESTRICT,
        related_name="player_stats",
        db_column="gsis_id",
    )
    season = IntegerField(null=False, blank=False)
    week = IntegerField(null=False, blank=False)
    team = ForeignKey(
        "teams.Teams",
        on_delete=RESTRICT,
        related_name="player_stats_team",
        name="team",
        db_column="team_id",
        default=""
    )
    opponent = ForeignKey(
        "teams.Teams",
        on_delete=RESTRICT,
        related_name="player_stats_opponent",
        name="opponent_team",
        db_column="opponent_team_id",
        default=""
    )
    completions = IntegerField(null=False, blank=False)
    attempts = IntegerField(null=False, blank=False)
    passing_yards = IntegerField(null=False, blank=False)
    passing_tds = IntegerField(null=False, blank=False)
    interceptions = IntegerField(null=False, blank=False)
    sacks = IntegerField(null=False, blank=False)
    sack_yards = IntegerField(null=False, blank=False)
    sack_fumbles = IntegerField(null=False, blank=False)
    sack_fumbles_lost = IntegerField(null=False, blank=False)
    passing_air_yards = IntegerField(null=False, blank=False)
    passing_yards_after_catch = IntegerField(null=False, blank=False)
    passing_first_downs = IntegerField(null=False, blank=False)
    passing_2pt_conversions = IntegerField(null=False, blank=False)
    carries = IntegerField(null=False, blank=False)
    rushing_yards = IntegerField(null=False, blank=False)
    rushing_tds = IntegerField(null=False, blank=False)
    rushing_fumbles = IntegerField(null=False, blank=False)
    rushing_fumbles_lost = IntegerField(null=False, blank=False)
    rushing_2pt_conversions = IntegerField(null=False, blank=False)
    rushing_first_downs = IntegerField(null=False, blank=False)
    receptions = IntegerField(null=True, blank=False)
    targets = IntegerField(null=True, blank=False)
    receiving_yards = IntegerField(null=False, blank=False)
    receiving_tds = IntegerField(null=False, blank=False)
    receiving_fumbles = IntegerField(null=False, blank=False)
    receiving_fumbles_lost = IntegerField(null=False, blank=False)
    receiving_yards_after_catch = IntegerField(null=False, blank=False)
    receiving_first_downs = IntegerField(null=False, blank=False)
    receiving_2pt_conversions = IntegerField(null=False, blank=False)
    receiving_target_share = FloatField(null=True, blank=True)
    special_teams_tds = IntegerField(null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.gsis_id.player_name}, {self.season}, Week {self.week}, {self.team}"