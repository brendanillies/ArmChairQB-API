from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from teams import views

urlpatterns = [
    # path("api/teams/", views.teams_list),
    # path("api/teams/<str:pk>/", views.teams_detail),  # Gets API
    # path("api/teams/<str:pk>/", views.teams_detail),  # Gets JSON
    path("api/teams/", views.TeamList.as_view()),
    path("api/teams/<str:team>", views.TeamList.as_view()),
    path("api/teams/<str:team>/", views.TeamList.as_view()),
    path(
        "api/teams/<str:team>/roster/week/<int:week>/",
        views.TeamWeeklyRosterList.as_view(),
    ),
    path(
        "api/teams/<str:team>/depth/week/<int:week>/",
        views.TeamWeeklyDepthChartList.as_view(),
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
