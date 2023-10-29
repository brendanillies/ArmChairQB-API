from players.serializers import RosterSerializer, DepthChartSerializer
from rest_framework import serializers

from .models import Teams


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = "__all__"


class TeamDepthChartSerializer(serializers.ModelSerializer):
    depth_chart = DepthChartSerializer(many=True, read_only=True, source="team_depth")

    class Meta:
        model = Teams
        fields = ["team", "depth_chart"]


class TeamRosterSerializer(serializers.ModelSerializer):
    roster = RosterSerializer(many=True, read_only=True, source="team_roster")

    class Meta:
        model = Teams
        fields = ["team", "roster"]
