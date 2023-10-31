from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from teams import views

urlpatterns = [
    path("api/teams/", views.TeamList.as_view(), name="team-list"),
    path("api/teams/<str:team>/", views.TeamDetail.as_view(), name="team-detail"),
    path(
        "api/teams/<str:team>/roster/",
        views.TeamRoster.as_view(),
        name="team-roster"
    ),
    path(
        "api/teams/<str:team>/depth/",
        views.TeamDepthChart.as_view(),
        name="team-depth"
    ),
    path(
        "api/teams/<str:team>/schedule/",
        views.TeamSchedule.as_view(),
        name="team-schedule"
    )
]

urlpatterns = format_suffix_patterns(urlpatterns)
