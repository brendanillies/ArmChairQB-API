from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from players import views

urlpatterns = [
    path("api/playerIdentifiers/", views.PlayerIdentifierList.as_view()),
    path("api/playerIdentifiers/<str:gsis_id>/", views.PlayerIdentifierDetail.as_view()),
    path(
        "api/stats/player/<str:gsis_id>/",
        views.PlayerStatsDetail.as_view(),
        name="player-stats"
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
