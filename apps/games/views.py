from rest_framework import generics

from .models import Schedule, Stadium
from .serializers import ScheduleSerializer


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
