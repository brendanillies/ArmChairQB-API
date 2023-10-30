from rest_framework import generics

from .models import PlayerIdentifier
from .serializers import PlayerIdentifierSerializer



class PlayerIdentifierList(generics.ListAPIView):
    """
    List all Player Identifier instances, or create a new Player Identifier instance
    """

    queryset = PlayerIdentifier.objects.all()
    serializer_class = PlayerIdentifierSerializer


class PlayerIdentifierDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a Player Identifier instance.
    """

    queryset = PlayerIdentifier.objects.all()
    serializer_class = PlayerIdentifierSerializer
    lookup_field = "gsis_id"
