from rest_framework import serializers

from apps.serializers import FilteredListSerializer

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
        list_serializer_class = FilteredListSerializer
        fields = "__all__"
        ordering = ["season", "week"]
