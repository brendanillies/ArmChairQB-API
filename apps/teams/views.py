from rest_framework import generics

from .models import Teams
from .serializers import TeamDepthChartSerializer, TeamRosterSerializer, TeamSerializer


class TeamList(generics.ListCreateAPIView):
    """
    List all Teams, or create a new Team
    """

    serializer_class = TeamSerializer
    lookup_field = "team"

    def get_queryset(self):
        team = self.kwargs.get("team", None)
        if team is not None:
            return Teams.objects.filter(team__icontains=team)
        return Teams.objects.all()


class TeamsAbstractInfoRetrieve(generics.RetrieveAPIView):
    """
    Abstract ListView of Teams-based objects
    """

    queryset = Teams.objects.all()
    lookup_url_kwarg = "team"

    def get_serializer_context(self):
        if "format" in self.kwargs:
            del self.kwargs["format"]
        context = {"request": self.kwargs}
        return context


class TeamWeeklyRosterList(TeamsAbstractInfoRetrieve):
    """
    This view returns a list of all Rostered players on a team
    filtered by week
    """

    serializer_class = TeamRosterSerializer


class TeamWeeklyDepthChartList(TeamsAbstractInfoRetrieve):
    """
    This view returns a team's Depth Chart filtered by week
    """

    serializer_class = TeamDepthChartSerializer


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
