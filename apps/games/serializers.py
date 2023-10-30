from rest_framework import serializers

from .models import Schedule, Stadium, PlayByPlay
from players.serializers import PlayerIdentifierSerializer


class ScheduleSerializer(serializers.ModelSerializer):
    home_team = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="team-detail", lookup_field="team"
    )
    away_team = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="team-detail", lookup_field="team"
    )

    class Meta:
        model = Schedule
        fields = "__all__"
        ordering = ["season", "week"]


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = "__all__"


class PlayByPlaySerializer(serializers.ModelSerializer):
    game_id = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="schedule-detail", lookup_field="game_id"
    )
    home_team = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="team-detail", lookup_field="team"
    )
    away_team = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="team-detail", lookup_field="team"
    )
    team_with_possession = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="team-detail", lookup_field="team"
    )
    timeout_team = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="team-detail", lookup_field="team"
    )
    touchdown_team = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="team-detail", lookup_field="team"
    )
    penalty_team = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="team-detail", lookup_field="team"
    )
    touchdown_gsis_id = PlayerIdentifierSerializer(
        read_only=True, source="pbp_touchdown_player"
    )
    fumbled_gsis_id = PlayerIdentifierSerializer(read_only=True, source="pbp_fumbler")
    passer_gsis_id = PlayerIdentifierSerializer(
        read_only=True, source="pbp_passing_player"
    )
    receiver_gsis_id = PlayerIdentifierSerializer(
        read_only=True, source="pbp_receiving_player"
    )
    rusher_gsis_id = PlayerIdentifierSerializer(
        read_only=True, source="pbp_rushing_player"
    )
    kicker_gsis_id = PlayerIdentifierSerializer(
        read_only=True, source="pbp_kicking_player"
    )
    penalty_gsis_id = PlayerIdentifierSerializer(
        read_only=True, source="pbp_penalty_player"
    )

    class Meta:
        model = PlayByPlay
        fields = "__all__"
