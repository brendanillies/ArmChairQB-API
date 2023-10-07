from rest_framework import serializers

from apps.serializers import FilteredListSerializer

from .models import DepthChart, PlayerIdentifier, Roster


class PlayerIdentifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerIdentifier
        fields = "__all__"


class DepthChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepthChart
        list_serializer_class = FilteredListSerializer
        fields = "__all__"


class RosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roster
        list_serializer_class = FilteredListSerializer
        fields = ["week", "player_name", "gsis_id", "position", "status"]
