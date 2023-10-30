from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from games import views

urlpatterns = [
    path("api/schedule/", views.ScheduleList.as_view(), name="schedule-list"),
    path(
        "api/schedule/<str:game_id>/",
        views.ScheduleDetail.as_view(),
        name="schedule-detail",
    ),
    path("api/stadium/", views.StadiumList.as_view(), name="stadium-list"),
    path("api/plays/", views.PlayByPlayList.as_view(), name="play-list")
]

urlpatterns = format_suffix_patterns(urlpatterns)
