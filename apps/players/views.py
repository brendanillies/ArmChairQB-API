from rest_framework import generics

from .models import PlayerIdentifier
from .serializers import PlayerIdentifierSerializer, StatsSerializer


class PlayerIdentifierList(generics.ListAPIView):
    """
    List all Player Identifier instances, or create a new Player Identifier instance
    """

    queryset = PlayerIdentifier.objects.all()
    serializer_class = PlayerIdentifierSerializer


class PlayerIdentifierDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a Player Identifier instance.
    """

    queryset = PlayerIdentifier.objects.all()
    serializer_class = PlayerIdentifierSerializer
    lookup_field = "gsis_id"


class PlayerStatsDetail(generics.RetrieveAPIView):
    """
    Lists all statistical field instances for a player
    """

    queryset = PlayerIdentifier.objects.all()
    serializer_class = StatsSerializer
    lookup_field = "gsis_id"

    # def get_queryset(self):
    #     return PlayerIdentifier.objects.filter(gsis_id=self.kwargs.get("gsis_id"))

    def get_serializer_context(self):
        context = super().get_serializer_context()

        query_params = {}
        for param, value in self.request.query_params.items():
            query_params[param] = value

        context["query_params"] = query_params
        return context
