from django.db import models
from django.db.models import (
    CharField,
    IntegerField,
    DateField,
    TimeField,
    ForeignKey,
    RESTRICT,
)
from datetime import time


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
        editable=False,
        name="divisional_game",
        verbose_name="divisional_game",
        db_column="divisional_game",
    )
    stadium_id = ForeignKey(Stadium, on_delete=RESTRICT, editable=False)
    surface = CharField(max_length=10, default="")
    roof = CharField(max_length=8, default="")

    def __str__(self) -> str:
        return f"{self.season} Week {self.week} - {self.away_team} vs. {self.home_team}"


class PlayByPlay(models.Model):
    class Meta:
        verbose_name_plural = "Play By Play"
        db_table = "PlayByPlay"

    game_id = ForeignKey(
        Schedule, related_name="pbp_game_ids", on_delete=RESTRICT, default=""
    )
    home_team = ForeignKey(
        "teams.Teams", related_name="pbp_home_team", on_delete=RESTRICT, default="", name="home_team_id"
    )
    away_team = ForeignKey(
        "teams.Teams", related_name="pbp_away_team", on_delete=RESTRICT, default="", name="away_team_id"
    )
    week = IntegerField(null=True, default=0)
    team_with_possession = ForeignKey(
        "teams.Teams",
        related_name="pbp_team_with_possession",
        on_delete=RESTRICT,
        default="",
    )
    side_of_field = CharField(max_length=4, default="", null=True)
    yardline_100 = IntegerField(null=True, default=0)
    quarter_seconds_remaining = IntegerField(null=False, default=0)
    half_seconds_remaining = IntegerField(null=False, default=0)
    game_seconds_remaining = IntegerField(null=False, default=0)
    half = CharField(max_length=8, default="", null=False)
    quarter_end = IntegerField(null=False, default=0)
    drive_num = IntegerField(default=0)
    quarter = IntegerField(null=False, default=0)
    down = IntegerField(null=True, default=0)
    yards_to_go = IntegerField(null=False, default=0)
    drive_net_yards = IntegerField(null=True, default=0)
    desc = CharField(
        max_length=750,
        null=False,
        name="play_description",
        db_column="play_description",
        default="",
    )
    play_type = CharField(max_length=20, default="", null=True)
    yards_gained = IntegerField(null=True, default=0)
    shotgun = IntegerField(null=True, default=0)
    no_huddle = IntegerField(null=True, default=0)
    qb_dropback = IntegerField(null=True, default=0)
    qb_kneel = IntegerField(null=True, default=0)
    qb_spike = IntegerField(null=True, default=0)
    qb_scramble = IntegerField(null=True, default=0)
    pass_length = CharField(max_length=7, null=True, default="")
    pass_location = CharField(max_length=7, null=True, default="")
    pass_air_yards = IntegerField(null=True, default=0)
    pass_yards_after_catch = IntegerField(null=True, default=0)
    run_location = CharField(max_length=7, null=True, default="")
    run_gap = CharField(max_length=7, null=True, default="")
    field_goal_result = CharField(max_length=7, null=True, default="")
    field_goal_kick_distance = IntegerField(null=True, default=0)
    extra_point_result = CharField(max_length=6, null=True, default="")
    two_point_conv_result = CharField(max_length=7, null=True, default="")
    home_timeouts_remaining = IntegerField(null=False, default=0)
    away_timeouts_remaining = IntegerField(null=False, default=0)
    timeout_taken = IntegerField(null=True, default=0)
    timeout_team = ForeignKey(
        "teams.Teams", related_name="pbp_timeout_team", on_delete=RESTRICT, default=""
    )
    touchdown_team = ForeignKey(
        "teams.Teams", related_name="pbp_touchdown_team", on_delete=RESTRICT, default=""
    )
    touchdown_gsis_id = ForeignKey(
        "players.PlayerIdentifier",
        related_name="pbp_touchdown_player",
        on_delete=RESTRICT,
        default="",
    )
    home_team_score = IntegerField(null=False, default=0)
    away_team_score = IntegerField(null=False, default=0)
    punt_blocked = IntegerField(null=True, default=0)
    rush_first_down = IntegerField(null=True, default=0)
    pass_first_down = IntegerField(null=True, default=0)
    third_down_converted = IntegerField(null=True, default=0)
    third_down_failed = IntegerField(null=True, default=0)
    fourth_down_converted = IntegerField(null=True, default=0)
    fourth_down_failed = IntegerField(null=True, default=0)
    pass_incomplete = IntegerField(null=True, default=0)
    kickoff_touchback = IntegerField(null=True, default=0)
    kickoff_inside_twenty = IntegerField(null=True, default=0)
    kickoff_in_endzone = IntegerField(null=True, default=0)
    kickoff_out_of_bounds = IntegerField(null=True, default=0)
    kickoff_downed = IntegerField(null=True, default=0)
    kickoff_fair_catch = IntegerField(null=True, default=0)
    pass_interception = IntegerField(null=True, default=0)
    punt_inside_twenty = IntegerField(null=True, default=0)
    punt_in_endzone = IntegerField(null=True, default=0)
    punt_out_of_bounds = IntegerField(null=True, default=0)
    punt_downed = IntegerField(null=True, default=0)
    punt_fair_catch = IntegerField(null=True, default=0)
    fumble_forced = IntegerField(null=True, default=0)
    fumble_not_forced = IntegerField(null=True, default=0)
    fumble_out_of_bounds = IntegerField(null=True, default=0)
    fumble_lost = IntegerField(null=True, default=0)
    fumble = IntegerField(null=True, default=0)
    fumbled_player_id = ForeignKey(
        "players.PlayerIdentifier",
        on_delete=RESTRICT,
        related_name="pbp_fumbler",
        default="",
    )
    tackle_solo = IntegerField(null=True, default=0)
    tackle_assist = IntegerField(null=True, default=0)
    safety = IntegerField(null=True, default=0)
    penalty = IntegerField(null=True, default=0)
    tackled_for_loss = IntegerField(null=True, default=0)
    own_kickoff_recovery = IntegerField(null=True, default=0)
    own_kickoff_recovery_touchdown = IntegerField(null=True, default=0)
    qb_hit = IntegerField(null=True, default=0)
    rush_attempt = IntegerField(null=True, default=0)
    pass_attempt = IntegerField(null=True, default=0)
    sack = IntegerField(null=True, default=0)
    touchdown = IntegerField(null=True, default=0)
    pass_touchdown = IntegerField(null=True, default=0)
    rush_touchdown = IntegerField(null=True, default=0)
    return_touchdown = IntegerField(null=True, default=0)
    extra_point_attempt = IntegerField(null=True, default=0)
    two_point_attempt = IntegerField(null=True, default=0)
    field_goal_attempt = IntegerField(null=True, default=0)
    kickoff_attempt = IntegerField(null=True, default=0)
    punt_attempt = IntegerField(null=True, default=0)
    pass_complete = IntegerField(null=True, default=0)
    passer_gsis_id = ForeignKey(
        "players.PlayerIdentifier",
        related_name="pbp_passing_player",
        on_delete=RESTRICT,
        default="",
    )
    pass_yards = IntegerField(null=True, default=0)
    receiver_gsis_id = ForeignKey(
        "players.PlayerIdentifier",
        related_name="pbp_receiving_player",
        on_delete=RESTRICT,
        default="",
    )
    rusher_gsis_id = ForeignKey(
        "players.PlayerIdentifier",
        related_name="pbp_rushing_player",
        on_delete=RESTRICT,
        default="",
    )
    rush_yards = IntegerField(null=True, default=0)
    kicker_gsis_id = ForeignKey(
        "players.PlayerIdentifier",
        related_name="pbp_kicking_player",
        on_delete=RESTRICT,
        default="",
    )
    penalty_team = ForeignKey(
        "teams.Teams", related_name="pbp_penalty_team", on_delete=RESTRICT, default=""
    )
    penalty_gsis_id = ForeignKey(
        "players.PlayerIdentifier",
        related_name="pbp_penalty_player",
        on_delete=RESTRICT,
        default="",
    )
    penalty_yards = IntegerField(null=True, default=0)
    penalty_type = CharField(max_length=75, null=True, default="")
    drive_result = CharField(max_length=25, null=True, default="")
    drive_play_count = IntegerField(null=True, default=0)
    drive_time_of_possession = TimeField(default=time())
    drive_first_downs = IntegerField(null=True, default=0)
    drive_inside_twenty = IntegerField(null=True, default=0)
    drive_ended_with_score = IntegerField(null=True, default=0)
    drive_quarter_start = IntegerField(null=True, default=0)
    drive_quarter_end = IntegerField(null=True, default=0)
    drive_yards_penalized = IntegerField(null=True, default=0)
    drive_start_transition = CharField(max_length=30, default="")
    drive_end_transition = CharField(max_length=30, default="")
    offense_formation = CharField(max_length=15, null=True, default="")
    offense_personnel = CharField(max_length=15, null=True, default="")
    defenders_in_box = IntegerField(null=True, default=0)
    defense_personnel = CharField(max_length=15, null=True, default="")
    defense_num_of_rushers = IntegerField(null=True, default=0)
    offense_player_gsis_ids = CharField(max_length=175, default="")
    defense_player_gsis_ids = CharField(max_length=175, default="")

    def save(self, *args, **kwargs):
        if self.play_type not in ("field_goal", "extra_point"):
            self.field_goal_kick_distance = 0

        super().save(*args, **kwargs)
