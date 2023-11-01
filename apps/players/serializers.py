from rest_framework import serializers

from apps.serializers import FilteredListSerializer, CustomModelSerializer

from .models import DepthChart, PlayerIdentifier, Roster


class PlayerIdentifierSerializer(serializers.ModelSerializer):
    gsis_id = serializers.HyperlinkedIdentityField(
        view_name="player-detail", lookup_field="gsis_id"
    )

    class Meta:
        model = PlayerIdentifier
        fields = "__all__"


class DepthChartSerializer(CustomModelSerializer):
    player = PlayerIdentifierSerializer(read_only=True, source="gsis_id")
    team = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="team-detail", lookup_field="team"
    )

    class Meta:
        model = DepthChart
        fields = "__all__"
        extra_fields = ["player"]


class RosterSerializer(CustomModelSerializer):
    player = PlayerIdentifierSerializer(read_only=True, source="gsis_id")
    team = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="team-detail", lookup_field="team"
    )

    class Meta:
        model = Roster
        fields = "__all__"
        extra_fields = ["player"]
