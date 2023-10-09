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


class PlayersAdmin(admin.ModelAdmin):
    change_list_template = "admin/players/change_list.html"

    @staticmethod
    def __clean_player_ids(file):
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

        # ids = (PlayerIdentifier(**record) for record in df.to_dict("records"))
        # PlayerIdentifier.objects.bulk_create(ids, batch_size=1000)
        return df

    @staticmethod
    def __clean_depth_charts(file):
        df = pd.read_csv(
            file,
            usecols=[
                "season",
                "club_code",
                "week",
                "depth_team",
                "formation",
                "gsis_id",
                "position",
                "depth_position",
            ],
        ).rename(columns={"club_code": "team_id", "depth_team": "depth"})
        df["team_id"].replace({"LA": "LAR"}, inplace=True)

        # objs = list()
        # for record in df.to_dict("records"):
        #     PlayerIdentifier.objects.get_or_create(
        #         gsis_id=record["gsis_id"],
        #         defaults={
        #             "espn_id": None,
        #             "yahoo_id": None,
        #             "name": record["full_name"],
        #             "db_season": None,
        #         },
        #     )

        #     objs.append(DepthChart(**record))

        # DepthChart.objects.bulk_create(objs, batch_size=1000)
        return df

    @staticmethod
    def __clean_rosters(file):
        df = pd.read_csv(
            file,
            usecols=[
                "season",
                "team",
                "position",
                "status",
                "week",
                "player_id",
                "espn_id",
                "yahoo_id",
            ],
        ).rename(
            columns={
                "team": "team_id",
                "player_id": "gsis_id",
                "headshot_url": "headshot",
            }
        )
        df["team_id"].replace({"LA": "LAR"}, inplace=True)

        # objs = list()
        # for record in df.to_dict("records"):
        #     PlayerIdentifier.objects.get_or_create(
        #         gsis_id=record["gsis_id"],
        #         defaults={
        #             "espn_id": None
        #             if pd.isna(record["espn_id"])
        #             else record["espn_id"],
        #             "yahoo_id": None
        #             if pd.isna(record["yahoo_id"])
        #             else record["yahoo_id"],
        #             "name": record["player_name"],
        #             "db_season": None,
        #         },
        #     )

        #     del record["espn_id"], record["yahoo_id"]
        #     objs.append(Roster(**record))

        # Roster.objects.bulk_create(objs, batch_size=1000)
        return df

    def __clean_files(
        self,
        player_ids: pd.DataFrame,
        depth_charts: pd.DataFrame,
        rosters: pd.DataFrame,
    ):
        player_ids = self.__clean_player_ids(player_ids)
        rosters = self.__clean_rosters(rosters)
        depth_charts = self.__clean_depth_charts(depth_charts)

        # Add any Player `gsis_id` not existent in player_ids from rosters & depth charts
        full = player_ids.merge(
            rosters[["gsis_id", "espn_id", "yahoo_id"]], how="outer", on="gsis_id"
        ).merge(depth_charts["gsis_id"], how="outer", on="gsis_id")
        full.to_csv("test.csv")

        # full = player_ids.merge(depth_charts, how="outer", on="gsis_id").merge(rosters, how="outer", on="gsis_id")

        return player_ids, depth_charts, rosters

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("import-csv/", self.upload_csv)]
        return new_urls + urls

    def upload_csv(self, request):
        # TODO: If records exist, bulk_update
        if request.method == "POST":
            player_ids = request.FILES["upload_player_identifier_file"]
            depth_charts = request.FILES["upload_depth_chart_file"]
            rosters = request.FILES["upload_roster_file"]

            player_ids, depth_charts, rosters = self.__clean_files(
                player_ids, depth_charts, rosters
            )

            # self.__create_player_identifier_objects(upload_player_identifier_file)

            # self.__create_depth_chart_objects(upload_depth_chart_file)

            # self.__create_roster_objects(upload_roster_file)

            self.message_user(request, "Your files have been imported")

        data = {
            "rosterForm": ImportCSVRosterForm(),
            "identifierForm": ImportCSVPlayerIdentifierForm(),
            "depthChartForm": ImportCSVDepthChartForm(),
        }

        return render(request, "admin/players/import-csv.html", data)


@admin.register(PlayerIdentifier)
class PlayerIdentifierAdmin(PlayersAdmin):
    list_display = ["player_name", "gsis_id", "espn_id", "yahoo_id", "college"]


@admin.register(Roster)
class RosterAdmin(PlayersAdmin):
    list_display = ["team", "season", "week", "status"]


@admin.register(DepthChart)
class DepthChartAdmin(PlayersAdmin):
    list_display = ["team", "season", "week", "depth", "position", "depth_position"]
