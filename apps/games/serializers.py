from rest_framework import serializers

from apps.serializers import FilteredListSerializer

from .models import Schedule, Stadium


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"


class ScheduleGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"


class ScheduleSeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        list_serializer_class = FilteredListSerializer
        fields = "__all__"


class ScheduleSeasonWeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        list_serializer_class = FilteredListSerializer
        fields = "__all__"


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = "__all__"
