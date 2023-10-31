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


class TeamStatDetail(generics.RetrieveAPIView):
    """
    Lists all statistical field instances for a team
    """

    queryset = Teams.objects.all()
    serializer_class = TeamStatSerializer
    lookup_field = "team"
