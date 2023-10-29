from django.contrib import admin
from django.forms import FileField, Form
from django.shortcuts import render
from django.urls import path
import pandas as pd

from .models import PlayerStats, TeamStats
from .upload import stats_mapper


class ImportCSVPlayerStatsForm(Form):
    upload_player_stats_file = FileField()


class StatsAdmin(admin.ModelAdmin):
    @admin.display(description="Team")
    def get_team(self, obj):
        return obj.team

    @admin.display(description="Opponent")
    def get_opponent_team(self, obj):
        return obj.opponent_team

    @staticmethod
    def __save_player_stats_objects(file):
        df = pd.read_csv(
            file,
            usecols=list(stats_mapper.keys()),
            dtype={key: val["dtype"] for key, val in stats_mapper.items()},
        ).rename(
            columns={
                key: val["name"]
                for key, val in stats_mapper.items()
                if val.get("name") is not None
            }
        )

        for field in df.filter(regex="(team_id)", axis=1).columns:
            df[field] = df[field].replace({"LA": "LAR"})

        objs = (PlayerStats(**record) for record in df.to_dict("records"))
        PlayerStats.objects.bulk_create(objs, batch_size=1000)

        return df

    @staticmethod
    def __save_team_stats_objects(df: pd.DataFrame):
        df.drop(columns=["gsis_id_id", "receiving_target_share"], inplace=True)
        df = df.groupby(["season", "week", "team_id", "opponent_team_id"], as_index=False).sum()

        objs = (TeamStats(**record) for record in df.to_dict("records"))
        TeamStats.objects.bulk_create(objs, batch_size=1000)

        return

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("import-csv/", self.upload_csv)]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            player_stats_file = request.FILES["upload_player_stats_file"]

            player_stats = self.__save_player_stats_objects(player_stats_file)
            self.__save_team_stats_objects(player_stats)

            self.message_user(request, "Your files have been imported")

        data = {"playerStatsForm": ImportCSVPlayerStatsForm()}

        return render(request, "admin/stats/import-csv.html", data)


@admin.register(PlayerStats)
class PlayerStatsAdmin(StatsAdmin):
    change_list_template = "admin/stats/change_list.html"
    list_display = ["get_player", "season", "week", "get_team", "get_opponent_team"]
    ordering = ["-season", "-week", "team"]
    search_fields = [
        "gsis_id__player_name__icontains",
        "team_id__team_name__icontains",
        "team_id__team__icontains",
    ]

    @admin.display(description="Player Name")
    def get_player(self, obj):
        return obj.gsis_id.player_name


@admin.register(TeamStats)
class TeamStatsAdmin(StatsAdmin):
    change_list_template = "admin/stats/change_list.html"
    list_display = ["season", "week", "get_team", "get_opponent_team"]
    ordering = ["-season", "-week", "team"]
    search_fields = [
        "team_id__team_name__icontains",
        "team_id__team__icontains",
    ]
