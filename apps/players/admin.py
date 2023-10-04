from django.contrib import admin
from django.forms import Form, FileField
from django.urls import path
from django.shortcuts import render
import pandas as pd
from .models import PlayerIdentifier, Roster, DepthChart


class ImportCSVRosterForm(Form):
    upload_roster_file = FileField()


class ImportCSVPlayerIdentifierForm(Form):
    upload_player_identifier_file = FileField()


class ImportCSVDepthChartForm(Form):
    upload_depth_chart_file = FileField()


@admin.register(PlayerIdentifier, Roster, DepthChart)
class PlayersAdmin(admin.ModelAdmin):
    change_list_template = "admin/players/change_list.html"

    @staticmethod
    def __create_player_identifier_objects(file):
        df = pd.read_csv(
            file,
            usecols=["gsis_id", "espn_id", "yahoo_id", "name", "db_season"],
            dtype={
                "espn_id": pd.Int32Dtype(),
                "yahoo_id": pd.Int32Dtype(),
                "db_season": pd.Int16Dtype(),
            },
        )
        df = df[~pd.isna(df["gsis_id"])]

        # Drop duplicates that don't have an `espn_id` or `yahoo_id`
        dup_df = df[df.duplicated(["gsis_id"], keep=False)]
        dup_df = dup_df[
            ~pd.isna(dup_df["gsis_id"])
            & (~pd.isna(dup_df["espn_id"]) | ~pd.isna(dup_df["yahoo_id"]))
        ]
        df.drop(index=dup_df.index, inplace=True)

        ids = (PlayerIdentifier(**record) for record in df.to_dict("records"))
        PlayerIdentifier.objects.bulk_create(ids, batch_size=1000)
        return

    @staticmethod
    def __create_depth_chart_objects(file):
        df = pd.read_csv(
            file,
            usecols=[
                "season",
                "club_code",
                "week",
                "game_type",
                "depth_team",
                "formation",
                "gsis_id",
                "jersey_number",
                "position",
                "depth_position",
                "full_name",
            ],
        ).rename(columns={"club_code": "club_code_id"})
        df["club_code_id"].replace({"LA": "LAR"}, inplace=True)

        objs = list()
        for record in df.to_dict("records"):
            PlayerIdentifier.objects.get_or_create(
                gsis_id=record["gsis_id"],
                defaults={
                    "espn_id": None,
                    "yahoo_id": None,
                    "name": record["full_name"],
                    "db_season": None,
                },
            )

            objs.append(DepthChart(**record))

        DepthChart.objects.bulk_create(objs, batch_size=1000)
        return

    @staticmethod
    def __create_roster_objects(file):
        df = pd.read_csv(
            file,
            usecols=[
                "season",
                "team",
                "position",
                "status",
                "player_name",
                "week",
                "game_type",
                "college",
                "player_id",
                "espn_id",
                "yahoo_id",
            ],
        ).rename(columns={"team": "team_id", "player_id": "gsis_id"})
        df["team_id"].replace({"LA": "LAR"}, inplace=True)

        objs = list()
        for record in df.to_dict("records"):
            PlayerIdentifier.objects.get_or_create(
                gsis_id=record["gsis_id"],
                defaults={
                    "espn_id": None
                    if pd.isna(record["espn_id"])
                    else record["espn_id"],
                    "yahoo_id": None
                    if pd.isna(record["yahoo_id"])
                    else record["yahoo_id"],
                    "name": record["player_name"],
                    "db_season": None,
                },
            )

            del record["espn_id"], record["yahoo_id"]
            objs.append(Roster(**record))

        Roster.objects.bulk_create(objs, batch_size=1000)
        return

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("import-csv/", self.upload_csv)]
        return new_urls + urls

    def upload_csv(self, request):
        # TODO: If records exist, bulk_update
        if request.method == "POST":
            upload_player_identifier_file = request.FILES[
                "upload_player_identifier_file"
            ]
            self.__create_player_identifier_objects(upload_player_identifier_file)

            upload_depth_chart_file = request.FILES["upload_depth_chart_file"]
            self.__create_depth_chart_objects(upload_depth_chart_file)

            upload_roster_file = request.FILES["upload_roster_file"]
            self.__create_roster_objects(upload_roster_file)

            self.message_user(request, "Your files have been imported")

        data = {
            "rosterForm": ImportCSVRosterForm(),
            "identifierForm": ImportCSVPlayerIdentifierForm(),
            "depthChartForm": ImportCSVDepthChartForm(),
        }

        return render(request, "admin/players/import-csv.html", data)
