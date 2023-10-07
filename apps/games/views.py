from rest_framework import generics

from .models import Schedule, Stadium
from .serializers import (
    ScheduleSerializer,
    ScheduleGameSerializer,
    ScheduleSeasonSerializer,
    ScheduleSeasonWeekSerializer,
    StadiumSerializer,
)


class ScheduleAbstractInfoList(generics.ListAPIView):
    queryset = Schedule.objects.all()

    def get_serializer_context(self):
        if "format" in self.kwargs:
            del self.kwargs["format"]
        context = {"request": self.kwargs}
        return context


class ScheduleList(ScheduleAbstractInfoList):
    """
    List all game instances
    """

    serializer_class = ScheduleSerializer


class ScheduleSeasonList(ScheduleAbstractInfoList):
    """
    List all game instances in a given season
    """

    serializer_class = ScheduleSeasonSerializer


class ScheduleSeasonWeekList(ScheduleAbstractInfoList):
    """
    List all game instances for a given week of a season
    """

    serializer_class = ScheduleSeasonWeekSerializer


class ScheduleGameDetail(generics.RetrieveAPIView):
    """
    Retrieve game detail by ESPN Game ID
    """

    queryset = Schedule.objects.all()
    serializer_class = ScheduleGameSerializer
    lookup_field = "espn_game_id"


class StadiumList(generics.ListAPIView):
    """
    List all stadiums (active and otherwise)
    """

    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer


class StadiumDetail(generics.RetrieveAPIView):
    """
    List all stadiums (active and otherwise)
    """

    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    lookup_field = "stadium_id"
