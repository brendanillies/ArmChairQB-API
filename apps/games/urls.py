from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from games import views

urlpatterns = [path("api/schedule/", views.ScheduleList.as_view(), name="schedufle-list")]

urlpatterns = format_suffix_patterns(urlpatterns)
