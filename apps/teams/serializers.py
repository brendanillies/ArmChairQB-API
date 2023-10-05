from rest_framework import serializers
# from .models import Teams
from django.apps import apps

Teams = apps.get_model(app_label='teams', model_name='Teams')


class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = ("team_abbr", "team_name", "team_division", "team_logo_squared")
