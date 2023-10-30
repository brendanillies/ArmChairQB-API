from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from players import views

urlpatterns = [
    path(
        "api/playerIdentifiers/",
        views.PlayerIdentifierList.as_view(),
        name="player-list"
    ),
    path(
        "api/playerIdentifiers/<str:gsis_id>/",
        views.PlayerIdentifierDetail.as_view(),
        name="player-detail"
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
