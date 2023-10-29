from rest_framework import serializers

from apps.serializers import FilteredListSerializer, CustomModelSerializer

from .models import PlayerStats


class PlayerStatsSerializer(CustomModelSerializer):
    team = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="team-detail", lookup_field="team"
    )
    opponent_team = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="team-detail", lookup_field="team"
    )

    class Meta:
        model = PlayerStats
        list_serializer_class = FilteredListSerializer
        fields = "__all__"
        extra_fields = ["team", "opponent_team"]
