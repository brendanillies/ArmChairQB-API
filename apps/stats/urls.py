from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from stats import views

urlpatterns = [
    path(
        "api/stats/player/<str:gsis_id>/",
        views.PlayerStatsDetail.as_view(),
        name="player-stats"
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
