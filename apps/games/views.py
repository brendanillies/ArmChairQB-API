from rest_framework import generics

from .models import Schedule, Stadium
from .serializers import ScheduleSerializer


class ScheduleAbstractInfoList(generics.ListAPIView):
    queryset = Schedule.objects.all()


class ScheduleList(ScheduleAbstractInfoList):
    """
    List all game instances
    """

    serializer_class = ScheduleSerializer
