from rest_framework import serializers

from apps.serializers import FilteredListSerializer

from .models import Schedule, Stadium


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        list_serializer_class = FilteredListSerializer
        fields = "__all__"
