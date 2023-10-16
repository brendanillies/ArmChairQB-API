from rest_framework import serializers

from apps.serializers import FilteredListSerializer

from .models import PlayerStats


class PlayerStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerStats
        list_serializer_class = FilteredListSerializer
        fields = "__all__"
