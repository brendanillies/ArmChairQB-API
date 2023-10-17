from datetime import datetime

import pandas as pd
from django.contrib import admin
from django.forms import FileField, Form
from django.shortcuts import render
from django.urls import path

from .models import PlayByPlay, Schedule, Stadium
from .upload import (
    play_by_play_mapper,
    play_by_play_times,
    schedule_mapper,
    schedule_datetimes,
)


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
            usecols=list(schedule_mapper.keys()) + schedule_datetimes,
            parse_dates=schedule_datetimes,
        ).rename(
            columns={
                key: val["name"]
                for key, val in play_by_play_mapper.items()
                if val.get("name") is not None
            }
        )
        df["home_team_id"].replace({"LA": "LAR"}, inplace=True)
        df["away_team_id"].replace({"LA": "LAR"}, inplace=True)
        df["overtime"].fillna(0, inplace=True)
        df["gameday"] = pd.to_datetime(df["gameday"], format="%Y-%m-%d")

        objs = (Schedule(**record) for record in df.to_dict("records"))

        Schedule.objects.bulk_create(objs)

        return

    @staticmethod
    def __create_play_by_play_objects(file):
        df = pd.read_csv(
            file,
            usecols=list(play_by_play_mapper.keys()) + play_by_play_times,
            dtype={key: val["dtype"] for key, val in play_by_play_mapper.items()},
            parse_dates=play_by_play_times,
            date_format="%M:%S",
        ).rename(
            columns={
                key: val["name"]
                for key, val in play_by_play_mapper.items()
                if val.get("name") is not None
            }
        )
        df["drive_time_of_possession"].fillna(datetime.min, inplace=True)
        df["season"] = df["game_id"].str.slice(stop=4).astype(int)

        mask = df["play_type"].isin(["field_goal", "extra_point"])
        df.loc[~mask, "field_goal_kick_distance"] = 0

        for field in df.filter(regex="(^(team)|team_id)", axis=1).columns:
            df[field] = df[field].replace({"LA": "LAR"})

        objs = (PlayByPlay(**record) for record in df.to_dict("records"))
        PlayByPlay.objects.bulk_create(objs, batch_size=1000)
        return

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("import-csv/", self.upload_csv)]
        return new_urls + urls

    def upload_csv(self, request):
        # TODO: If records exist, bulk_update
        if request.method == "POST":
            schedule_file = request.FILES["upload_schedule_file"]
            self.__create_stadium_objects(schedule_file)
            self.__create_schedule_objects(schedule_file)

            pbp_file = request.FILES["upload_play_by_play_file"]
            self.__create_play_by_play_objects(pbp_file)

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
    @admin.display(description="Stadium")
    def get_stadium(self, obj):
        return obj.stadium_id.name

    list_display = [
        "game_id",
        "season",
        "week",
        "away_team",
        "home_team",
        "get_stadium",
        "divisional_game",
    ]
    search_fields = [
        "season",
        "home_team__team__icontains",
        "home_team__team_name__icontains",
        "away_team__team__icontains",
        "away_team__team_name__icontains",
    ]


@admin.register(PlayByPlay)
class PlayByPlayAdmin(GamesAdmin):
    ordering = ["-season", "-week", "home_team", "quarter", "-game_seconds_remaining"]
    list_display = [
        "game_id",
        "season",
        "week",
        "away_team",
        "home_team",
        "quarter",
        "game_seconds_remaining",
    ]
