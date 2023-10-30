from rest_framework import serializers

from apps.serializers import FilteredListSerializer, CustomModelSerializer

from .models import PlayerStats, TeamStats
from players.models import PlayerIdentifier
from teams.models import Teams


class _PlayerStatSerializer(CustomModelSerializer):
    team = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="team-detail", lookup_field="team"
    )
    opponent_team = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="team-detail", lookup_field="team"
    )

    class Meta:
        model = PlayerStats
        exclude = ["gsis_id"]


class _TeamStatSerializer(CustomModelSerializer):
    opponent_team = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="team-detail", lookup_field="team"
    )

    class Meta:
        model = TeamStats
        exclude = ["team"]


class PlayerStatSerializer(CustomModelSerializer):
    stats = _PlayerStatSerializer(read_only=True, many=True, source="player_stats")

    class Meta:
        model = PlayerIdentifier
        list_serializer_class = FilteredListSerializer
        fields = "__all__"


class TeamStatSerializer(CustomModelSerializer):
    team = serializers.HyperlinkedIdentityField(
        view_name="team-detail", lookup_field="team"
    )

    stats = _TeamStatSerializer(read_only=True, many=True, source="team_stats_team")

    class Meta:
        model = Teams
        list_serializer_class = FilteredListSerializer
        fields = "__all__"
