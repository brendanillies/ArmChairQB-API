from rest_framework import generics

from .models import Schedule, Stadium, PlayByPlay
from .serializers import ScheduleSerializer, StadiumSerializer, PlayByPlaySerializer


class ScheduleList(generics.ListAPIView):
    """
    List all game instances
    """

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleDetail(generics.RetrieveAPIView):
    """
    Retrieve specific game instance
    """

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    lookup_field = "game_id"


class StadiumList(generics.ListAPIView):
    """
    List all stadium instances
    """

    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer


class PlayByPlayList(generics.ListAPIView):
    """
    List all plays
    """
    queryset = PlayByPlay.objects.all()
    serializer_class = PlayByPlaySerializer