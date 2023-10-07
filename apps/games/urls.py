from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from games import views

urlpatterns = [
    path("api/schedule/", views.ScheduleList.as_view()),
    path("api/schedule/season/<int:season>/", views.ScheduleSeasonList.as_view()),
    path("api/schedule/season/<int:season>/week/<int:week>", views.ScheduleSeasonWeekList.as_view()),
    path("api/schedule/game/<int:espn_game_id>/", views.ScheduleGameDetail.as_view()),
    path("api/stadium", views.StadiumList.as_view()),
    path("api/stadium/<str:stadium_id>", views.StadiumDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
