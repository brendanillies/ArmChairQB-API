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

    def get_serializer_context(self):
        if "format" in self.kwargs:
            del self.kwargs["format"]
        context = {"request": self.kwargs}
        return context


class PlayerStatsDetail(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    """
    List all statistical field instances for a Player Identifier Instance with season and week filters
    """

    queryset = PlayerStats.objects.all()
    serializer_class = PlayerStatsSerializer
    lookup_fields = ("gsis_id", "season", "week")
