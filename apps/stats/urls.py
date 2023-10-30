from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from stats import views

urlpatterns = [
    path(
        "api/stats/player/<str:gsis_id>/",
        views.PlayerStatDetail.as_view(),
        name="player-stats"
    ),
    path(
        "api/stats/team/<str:team>/",
        views.TeamStatDetail.as_view(),
        name="team-stats"
    )
]

urlpatterns = format_suffix_patterns(urlpatterns)
