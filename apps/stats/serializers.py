from rest_framework import serializers

from apps.serializers import FilteredListSerializer, CustomModelSerializer

from .models import PlayerStats
from players.models import PlayerIdentifier


# class PlayerStatsSerializer(CustomModelSerializer):
#     team = serializers.HyperlinkedRelatedField(
#         read_only=True, view_name="team-detail", lookup_field="team"
#     )
#     opponent_team = serializers.HyperlinkedRelatedField(
#         read_only=True, view_name="team-detail", lookup_field="team"
#     )

#     class Meta:
#         model = PlayerStats
#         list_serializer_class = FilteredListSerializer
#         fields = "__all__"


class _PlayerStatSerializer(CustomModelSerializer):
    class Meta:
        model = PlayerStats
        fields = "__all__"


class PlayerStatSerializer(CustomModelSerializer):
    stats = _PlayerStatSerializer(read_only=True, many=True, source="player_stats")

    class Meta:
        model = PlayerIdentifier
        list_serializer_class = FilteredListSerializer
        fields = "__all__"
