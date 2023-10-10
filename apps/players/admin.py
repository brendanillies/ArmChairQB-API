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
            usecols=["gsis_id", "espn_id", "yahoo_id", "name", "db_season", "college"],
            dtype={
                "espn_id": pd.Int32Dtype(),
                "yahoo_id": pd.Int32Dtype(),
                "db_season": pd.Int16Dtype(),
            },
        ).rename(columns={"name": "player_name"})
        df = df[~pd.isna(df["gsis_id"])]

        # Drop duplicates that don't have an `espn_id` or `yahoo_id`
        dup_df = df[df.duplicated(["gsis_id"], keep=False)]
        dup_df = dup_df[
            ~pd.isna(dup_df["gsis_id"])
            & (~pd.isna(dup_df["espn_id"]) | ~pd.isna(dup_df["yahoo_id"]))
        ]
        df.drop(index=dup_df.index, inplace=True)

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
        ).rename(
            columns={
                "club_code": "team_id",
                "depth_team": "depth",
                "gsis_id": "gsis_id_id",
            }
        )
        df["team_id"].replace({"LA": "LAR"}, inplace=True)

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
            dtype={
                "espn_id": pd.Int32Dtype(),
                "yahoo_id": pd.Int32Dtype(),
            }
        ).rename(
            columns={
                "team": "team_id",
                "player_id": "gsis_id_id",
                "headshot_url": "headshot",
            }
        )
        df["team_id"].replace({"LA": "LAR"}, inplace=True)

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
        player_ids = player_ids.merge(
            rosters[["gsis_id_id", "espn_id", "yahoo_id"]].rename(
                columns={"gsis_id_id": "gsis_id"}
            ),
            how="outer",
            on="gsis_id",
        ).merge(
            depth_charts["gsis_id_id"].rename("gsis_id"),
            how="outer",
            on="gsis_id",
        )
        for col in ["espn_id", "yahoo_id"]:
            player_ids[col] = player_ids[f"{col}_x"].fillna(player_ids[f"{col}_y"])
            player_ids.drop(
                columns=[f"{col}_{merge_col}" for merge_col in ("x", "y")], inplace=True
            )

        player_ids = player_ids.drop_duplicates()

        # Drop unnecessary columns from file objects
        roster_fields = [field.name for field in Roster._meta.get_fields()]
        roster_fields.extend(["gsis_id_id", "team_id"])  # Id fields
        rosters.drop(
            columns=[
                field
                for field in rosters.columns
                if field not in roster_fields
            ],
            inplace=True
        )
        return player_ids, depth_charts, rosters

    @staticmethod
    def __save_objects(
        player_ids: pd.DataFrame, depth_charts: pd.DataFrame, rosters: pd.DataFrame
    ):
        # PlayerIdentifier object upload
        objs = (PlayerIdentifier(**record) for record in player_ids.to_dict("records"))
        PlayerIdentifier.objects.bulk_create(objs, batch_size=1000)

        # DepthChart object upload
        objs = (DepthChart(**record) for record in depth_charts.to_dict("records"))
        DepthChart.objects.bulk_create(objs, batch_size=1000)

        # Roster object upload
        objs = (Roster(**record) for record in rosters.to_dict("records"))
        Roster.objects.bulk_create(objs, batch_size=1000)

        return

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

            self.__save_objects(player_ids, depth_charts, rosters)

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
