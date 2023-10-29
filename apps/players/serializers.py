from rest_framework import serializers

from apps.serializers import FilteredListSerializer, CustomModelSerializer

from .models import DepthChart, PlayerIdentifier, Roster


class PlayerIdentifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerIdentifier
        fields = ["gsis_id", "espn_id", "yahoo_id", "headshot", "age", "player_name"]


class DepthChartSerializer(CustomModelSerializer):
    player = PlayerIdentifierSerializer(read_only=True, source="gsis_id")

    class Meta:
        model = DepthChart
        list_serializer_class = FilteredListSerializer
        fields = "__all__"
        extra_fields = ["player"]


class RosterSerializer(CustomModelSerializer):
    player = PlayerIdentifierSerializer(read_only=True, source="gsis_id")

    class Meta:
        model = Roster
        list_serializer_class = FilteredListSerializer
        fields = "__all__"
        extra_fields = ["player"]
