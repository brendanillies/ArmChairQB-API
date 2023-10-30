from rest_framework import generics

from apps.mixins import MultipleFieldLookupMixin

from players.models import PlayerIdentifier
from teams.models import Teams
from .serializers import TeamStatSerializer, PlayerStatSerializer


class PlayerStatDetail(generics.RetrieveAPIView):
    """
    Lists all statistical field instances for a player
    """

    queryset = PlayerIdentifier.objects.all()
    serializer_class = PlayerStatSerializer
    lookup_field = "gsis_id"

    def get_serializer_context(self):
        context = super().get_serializer_context()

        query_params = {}
        for param, value in self.request.query_params.items():
            query_params[param] = value

        context["query_params"] = query_params
        return context


class TeamStatDetail(generics.RetrieveAPIView):
    """
    Lists all statistical field instances for a player
    """

    queryset = Teams.objects.all()
    serializer_class = TeamStatSerializer
    lookup_field = "team"

    def get_serializer_context(self):
        context = super().get_serializer_context()

        query_params = {}
        for param, value in self.request.query_params.items():
            query_params[param] = value

        context["query_params"] = query_params
        return context
