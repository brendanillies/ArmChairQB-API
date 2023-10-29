from players.serializers import RosterSerializer, DepthChartSerializer
from games.serializers import ScheduleSerializer
from apps.serializers import CustomModelSerializer, CustomHyperlinkedModelSerializer
from rest_framework import serializers

from .models import Teams


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = "__all__"


class TeamDepthChartSerializer(CustomModelSerializer):
    depth_chart = DepthChartSerializer(many=True, read_only=True, source="team_depth")
    team = serializers.HyperlinkedIdentityField(view_name="team-detail", lookup_field="team")

    class Meta:
        model = Teams
        fields = "__all__"
        extra_fields = ["depth_chart"]


class TeamRosterSerializer(CustomModelSerializer):
    roster = RosterSerializer(many=True, read_only=True, source="team_roster")
    team = serializers.HyperlinkedIdentityField(view_name="team-detail", lookup_field="team")

    class Meta:
        model = Teams
        fields = "__all__"
        extra_fields = ["roster"]


class TeamScheduleSerializer(CustomModelSerializer):
    away_games = ScheduleSerializer(many=True, read_only=True, source="schedule_away")
    home_games = ScheduleSerializer(many=True, read_only=True, source="schedule_home")
    team = serializers.HyperlinkedIdentityField(view_name="team-detail", lookup_field="team")

    class Meta:
        model = Teams
        fields = "__all__"
        extra_fields = ["away_games", "home_games"]
