from rest_framework import generics
from rest_framework import filters

from .models import Teams
from .serializers import (
    TeamDepthChartSerializer,
    TeamRosterSerializer,
    TeamSerializer,
    TeamScheduleSerializer,
)


class TeamList(generics.ListAPIView):
    """
    List all Teams, or create a new Team
    """

    queryset = Teams.objects.all()
    serializer_class = TeamSerializer
    lookup_field = "team"
    filter_backends = [filters.SearchFilter]
    search_fields = ["team", "team_name", "team_nick", "team_division"]


class TeamDetail(generics.RetrieveAPIView):
    """
    List all Teams, or create a new Team
    """

    queryset = Teams.objects.all()
    serializer_class = TeamSerializer
    lookup_field = "team"


class TeamAbstractInfoRetrieve(generics.RetrieveAPIView):
    """
    Abstract ListView of Team Roster or DepthChart objects
    """

    queryset = Teams.objects.all()
    lookup_field = "team"


class TeamRoster(TeamAbstractInfoRetrieve):
    """
    Returns all rostered players for a team
    """

    serializer_class = TeamRosterSerializer


class TeamDepthChart(TeamAbstractInfoRetrieve):
    """
    Returns a team's depth chart
    """

    serializer_class = TeamDepthChartSerializer


class TeamSchedule(TeamAbstractInfoRetrieve):
    """
    Returns a team's schedule
    """

    serializer_class = TeamScheduleSerializer


# @api_view(["GET", "POST"])
# def teams_list(request, format=None):
#     """
#     List all NFL Teams, or create a new Team
#     """
#     if request.method == "GET":
#         teams = Teams.objects.all()
#         serializer = TeamsSerializer(teams, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = TeamsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "PUT", "DELETE"])
# def teams_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a Team.
#     """
#     print(pk, format)
#     try:
#         teams = Teams.objects.get(pk=pk)
#     except Teams.DoesNotExist:
#         return Response(status=status.HTTP_400_BAD_REQUEST)

#     if request.method == "GET":
#         serializer = TeamsSerializer(teams)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = TeamsSerializer(teams, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         teams.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
