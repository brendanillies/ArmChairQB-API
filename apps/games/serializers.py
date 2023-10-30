from rest_framework import serializers

from .models import Schedule, Stadium


class ScheduleSerializer(serializers.ModelSerializer):
    home_team = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="team-detail", lookup_field="team"
    )
    away_team = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="team-detail", lookup_field="team"
    )

    class Meta:
        model = Schedule
        fields = "__all__"
        ordering = ["season", "week"]


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = "__all__"
