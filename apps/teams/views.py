from rest_framework import generics

from .models import Teams
from .serializers import (TeamDepthChartSerializer, TeamRosterSerializer,
                          TeamSerializer)


class TeamList(generics.ListCreateAPIView):
    """
    List all Teams, or create a new Team
    """

    queryset = Teams.objects.all()
    serializer_class = TeamSerializer


class TeamWeeklyRosterList(generics.ListAPIView):
    """
    This view returns a list of all Rostered players on a team
    filtered by week
    """

    serializer_class = TeamRosterSerializer

    def get_queryset(self):
        return Teams.objects.filter(team_abbr=self.kwargs["pk"])

    def get_serializer_context(self):
        context = {"request": self.kwargs}
        return context


class TeamWeeklyDepthChartList(generics.ListAPIView):
    """
    This view returns a list of all Rostered players on a team
    filtered by week
    """

    serializer_class = TeamDepthChartSerializer

    def get_queryset(self):
        return Teams.objects.filter(team_abbr=self.kwargs["pk"])

    def get_serializer_context(self):
        context = {"request": self.kwargs}
        return context


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a Teams instance.
    """

    queryset = Teams.objects.all()
    serializer_class = TeamSerializer


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
