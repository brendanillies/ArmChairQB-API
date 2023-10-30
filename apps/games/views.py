from rest_framework import generics

from .models import Schedule, Stadium
from .serializers import ScheduleSerializer, StadiumSerializer


class ScheduleList(generics.ListAPIView):
    """
    List all game instances
    """

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class StadiumList(generics.ListAPIView):
    """
    List all stadium instances
    """

    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
