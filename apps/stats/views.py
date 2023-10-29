from rest_framework import generics

from apps.mixins import MultipleFieldLookupMixin

from .models import PlayerStats
from .serializers import PlayerStatsSerializer


class PlayerStatsList(generics.ListAPIView):
    """
    List all statistical field instances for a Player Identifier Instance
    """

    queryset = PlayerStats.objects.all()
    serializer_class = PlayerStatsSerializer


class PlayerStatsDetail(generics.ListAPIView):
    """
    Lists all statistical field instances for a player
    """

    serializer_class = PlayerStatsSerializer
    lookup_field = "gsis_id"

    def get_queryset(self):
        return PlayerStats.objects.filter(gsis_id=self.kwargs.get("gsis_id"))

    def get_serializer_context(self):
        context = super().get_serializer_context()

        query_params = {}
        for param, value in self.request.query_params.items():
            query_params[param] = value

        context["query_params"] = query_params
        return context
