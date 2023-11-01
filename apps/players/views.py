from rest_framework import generics
import django_filters

from .models import PlayerIdentifier, Roster, DepthChart
from .filters import RosterFilter, DepthChartFilter
from .serializers import (
    PlayerIdentifierSerializer,
    RosterSerializer,
    DepthChartSerializer,
)


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


class RosterList(generics.ListAPIView):
    """
    List all Roster instances matching given query
    """

    queryset = Roster.objects.all()
    serializer_class = RosterSerializer
    filterset_class = RosterFilter


class DepthChartList(generics.ListAPIView):
    """
    List all Depth Chart instances matching given query
    """

    queryset = DepthChart.objects.all()
    serializer_class = DepthChartSerializer
    filterset_class = DepthChartFilter
