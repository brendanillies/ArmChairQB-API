from .serializers import TeamsSerializer
from django.apps import apps
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

Teams = apps.get_model(app_label="teams", model_name="Teams")

# Create your views here.


# class TeamsView(viewsets.ModelViewSet):
#     serializer_class = TeamsSerializer
#     queryset = Teams.objects.all()


@csrf_exempt
def teams_list(request):
    """
    List all NFL Teams, or create a new Team
    """
    if request.method == "GET":
        teams = Teams.objects.all()
        serializer = TeamsSerializer(teams, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = TeamsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def teams_detail(request, pk):
    """
    Retrieve, update or delete a team.
    """
    try:
        teams = Teams.objects.get(pk=pk)
    except Teams.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = TeamsSerializer(teams)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = TeamsSerializer(teams, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        teams.delete()
        return HttpResponse(status=204)
