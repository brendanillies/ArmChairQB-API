from rest_framework import generics, filters
import django_filters.rest_framework as dj_filters

from .models import Teams
from .serializers import TeamSerializer, TeamScheduleSerializer
from .filters import TeamFilter


class TeamList(generics.ListAPIView):
    """
    List all Teams, or create a new Team
    """

    queryset = Teams.objects.all()
    serializer_class = TeamSerializer
    filter_backends = [filters.SearchFilter, dj_filters.DjangoFilterBackend]
    search_fields = ["team", "team_name", "team_nick"]
    filterset_class = TeamFilter


class TeamDetail(generics.RetrieveAPIView):
    """
    List all Teams, or create a new Team
    """

    queryset = Teams.objects.all()
    serializer_class = TeamSerializer
    lookup_field = "team"


class TeamSchedule(generics.RetrieveAPIView):
    """
    Returns a team's schedule
    """

    queryset = Teams.objects.all()
    serializer_class = TeamScheduleSerializer
    lookup_field = "team"
