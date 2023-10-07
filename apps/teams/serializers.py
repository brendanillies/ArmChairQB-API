from players.serializers import RosterSerializer, DepthChartSerializer
from rest_framework import serializers

from .models import Teams


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = "__all__"


class TeamDepthChartSerializer(serializers.ModelSerializer):
    team_depth = DepthChartSerializer(many=True, read_only=True)

    class Meta:
        model = Teams
        fields = ["team", "team_depth"]


class TeamRosterSerializer(serializers.ModelSerializer):
    team_roster = RosterSerializer(many=True, read_only=True)

    class Meta:
        model = Teams
        fields = ["team", "team_roster"]
