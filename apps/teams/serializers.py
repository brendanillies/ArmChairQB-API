from games.serializers import ScheduleSerializer
from apps.serializers import CustomModelSerializer, CustomHyperlinkedModelSerializer
from rest_framework import serializers

from .models import Teams


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = "__all__"


class TeamScheduleSerializer(CustomModelSerializer):
    away_games = ScheduleSerializer(many=True, read_only=True, source="schedule_away")
    home_games = ScheduleSerializer(many=True, read_only=True, source="schedule_home")
    team = serializers.HyperlinkedIdentityField(view_name="team-detail", lookup_field="team")

    class Meta:
        model = Teams
        fields = "__all__"
        extra_fields = ["away_games", "home_games"]
