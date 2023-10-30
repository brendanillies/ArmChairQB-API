from rest_framework import generics

from .models import Schedule, Stadium
from .serializers import ScheduleSerializer


class ScheduleList(generics.ListAPIView):
    """
    List all game instances
    """

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
