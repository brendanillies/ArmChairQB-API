from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from games import views

urlpatterns = [
    path("api/schedules/", views.ScheduleList.as_view(), name="schedule-list"),
    path("api/stadiums/", views.StadiumList.as_view(), name="stadium-list"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
