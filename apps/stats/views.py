from rest_framework import generics

from apps.mixins import MultipleFieldLookupMixin

from .models import PlayerStats
from players.models import PlayerIdentifier
from .serializers import PlayerStatsSerializer
