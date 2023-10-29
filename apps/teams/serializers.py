from players.serializers import RosterSerializer, DepthChartSerializer
from games.serializers import ScheduleSerializer
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


class TeamScheduleSerializer(serializers.ModelSerializer):
    away_games = ScheduleSerializer(many=True, read_only=True, source="schedule_away")
    home_games = ScheduleSerializer(many=True, read_only=True, source="schedule_home")

    class Meta:
        model = Teams
        fields = ["team", "away_games", "home_games"]
