from django.urls import path
from teams import views

urlpatterns = [
    path("teams/", views.teams_list),
    path("teams/<str:pk>/", views.teams_detail),
]
