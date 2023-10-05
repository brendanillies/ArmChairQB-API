from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TeamsSerializer
from django.apps import apps

Teams = apps.get_model(app_label='teams', model_name='Teams')

# Create your views here.


class TeamsView(viewsets.ModelViewSet):
    serializer_class = TeamsSerializer
    queryset = Teams.objects.all()
