from django.contrib import admin
from django.forms import FileField, Form
from django.shortcuts import render
from django.urls import path
import pandas as pd

from .models import PlayerStats
from .util import stats_mapper


class ImportCSVPlayerStatsForm(Form):
    upload_player_stats_file = FileField()


@admin.register(PlayerStats)
class PlayerStatsAdmin(admin.ModelAdmin):
    change_list_template = "admin/stats/change_list.html"
    list_display = ["get_player", "season", "week", "team", "opponent_team"]
    ordering = ["-season", "-week", "team"]
    search_fields = [
        "gsis_id__player_name__icontains",
        "team_id__team_name__icontains",
        "team_id__team__icontains",
    ]

    @admin.display(description="Player Name")
    def get_player(self, obj):
        return obj.gsis_id.player_name

    @staticmethod
    def __save_objects(file):
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

        return

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("import-csv/", self.upload_csv)]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            player_stats = request.FILES["upload_player_stats_file"]

            self.__save_objects(player_stats)

            self.message_user(request, "Your files have been imported")

        data = {"playerStatsForm": ImportCSVPlayerStatsForm()}

        return render(request, "admin/stats/import-csv.html", data)
