from rest_framework import generics
from rest_framework import filters

from .models import Teams
from .serializers import TeamSerializer, TeamScheduleSerializer


class TeamList(generics.ListAPIView):
    """
    List all Teams, or create a new Team
    """

    queryset = Teams.objects.all()
    serializer_class = TeamSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["team", "team_name", "team_nick", "team_division"]


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
