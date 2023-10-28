from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from stats import views

urlpatterns = [
    path(
        "api/playerStats/playerIdentifier/<str:gsis_id>/",
        views.PlayerStatsList.as_view(),
    ),
    path(
        "api/playerStats/playerIdentifier/<str:gsis_id>/season/<int:season>/",
        views.PlayerStatsList.as_view(),
    ),
    path(
        "api/playerStats/playerIdentifier/<str:gsis_id>/season/<int:season>/week/<int:week>/",
        views.PlayerStatsDetail.as_view(),
    ),
    # path(
    #     "api/playerStats/position/<str:position>/season/<int:season>",
    #     views.PlayerStatsList.as_view(),
    # ),
    # path(
    #     "api/playerStats/position/<str:position>/season/<int:season>/week/<int:week>",
    #     views.PlayerStatsList.as_view(),
    # ),
]

urlpatterns = format_suffix_patterns(urlpatterns)