from django.contrib import admin
from django.forms import Form, FileField
from django.urls import path
from django.shortcuts import render
from .models import PlayByPlay, Schedule, Stadium
import pandas as pd


class ImportCSVPlayByPlayForm(Form):
    upload_play_by_play_file = FileField()


class ImportCSVScheduleForm(Form):
    upload_schedule_file = FileField()


class GamesAdmin(admin.ModelAdmin):
    change_list_template = "admin/games/change_list.html"

    @staticmethod
    def __create_stadium_objects(file):
        df = (
            pd.read_csv(file, usecols=["stadium_id", "stadium"])
            .rename(columns={"stadium": "name"})
            .drop_duplicates()
        )

        objs = (Stadium(**record) for record in df.to_dict("records"))

        Stadium.objects.bulk_create(objs)

        return

    @staticmethod
    def __create_schedule_objects(file):
        file.file.seek(0)

        df = pd.read_csv(
            file,
            usecols=[
                "game_id",
                "season",
                "game_type",
                "week",
                "gameday",
                "weekday",
                "gametime",
                "away_team",
                "home_team",
                "location",
                "overtime",
                "espn",
                "div_game",
                "stadium_id",
                "surface",
                "roof",
            ],
            parse_dates=["gameday"],
        ).rename(
            columns={
                "away_team": "away_team_id",
                "home_team": "home_team_id",
                "stadium_id": "stadium_id_id",
                "espn": "espn_game_id",
            }
        )
        df["home_team_id"].replace({"LA": "LAR"}, inplace=True)
        df["away_team_id"].replace({"LA": "LAR"}, inplace=True)
        df["overtime"].fillna(0, inplace=True)
        df["gameday"] = pd.to_datetime(df["gameday"], format="%Y-%m-%d")

        objs = (Schedule(**record) for record in df.to_dict("records"))

        Schedule.objects.bulk_create(objs)

        return

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("import-csv/", self.upload_csv)]
        return new_urls + urls

    def upload_csv(self, request):
        # TODO: If records exist, bulk_update
        if request.method == "POST":
            upload_schedule_file = request.FILES["upload_schedule_file"]
            self.__create_stadium_objects(upload_schedule_file)
            self.__create_schedule_objects(upload_schedule_file)

            self.message_user(request, "Your files have been imported")

        data = {
            "playByPlayForm": ImportCSVPlayByPlayForm(),
            "scheduleForm": ImportCSVScheduleForm(),
        }

        return render(request, "admin/games/import-csv.html", data)


@admin.register(Stadium)
class StadiumAdmin(GamesAdmin):
    list_display = ["name", "stadium_id"]
    search_fields = ["name"]


@admin.register(Schedule)
class ScheduleAdmin(GamesAdmin):
    @admin.display(description="Away Team")
    def get_away_team(self, obj):
        return obj.away_team.team

    @admin.display(description="Home Team")
    def get_home_team(self, obj):
        return obj.home_team.team

    @admin.display(description="Stadium")
    def get_stadium(self, obj):
        return obj.stadium_id.name

    list_display = [
        "game_id",
        "season",
        "week",
        "get_away_team",
        "get_home_team",
        "get_stadium",
        "divisional_game",
    ]
    search_fields = [
        "season",
        "home_team_id__team__icontains",
        "away_team_id__team__icontains",
    ]


@admin.register(PlayByPlay)
class PlayByPlayAdmin(GamesAdmin):
    ...
