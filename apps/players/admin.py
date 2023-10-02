from django.contrib import admin
from django.forms import Form, FileField
from django.urls import path
from django.shortcuts import render
import pandas as pd
from .models import Player, PlayerIdentifier, Roster, DepthChart


class ImportCSVForm(Form):
    csv_file = FileField()


admin.site.register(PlayerIdentifier)
admin.site.register(Roster)
admin.site.register(DepthChart)
admin.site.register(Player)


class PlayerIdentifierAdmin(admin.ModelAdmin):
    change_list_template = "admin/players/change_list.html"


class RosterAdmin(admin.ModelAdmin):
    change_list_template = "admin/players/change_list.html"


class DepthChartAdmin(admin.ModelAdmin):
    change_list_template = "admin/players/change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("import-csv/", self.upload_csv)]
        return new_urls + urls

    def upload_csv(self, request):
        # TODO: If records exist, bulk_update
        if request.method == "POST":
            print(request)
            csv_file = request.FILES["csv_file"]
            self.message_user(request, "CSV file has been captured")

            df = pd.read_csv(csv_file)
            # teams = (
            #     Teams(**record) for record in df.to_dict('records')
            # )
            # Teams.objects.bulk_create(teams)

            # self.message_user(request, "Your csv file has been imported")

        form = ImportCSVForm()
        data = {"form": form}

        return render(request, "admin/import-csv.html", data)


# @admin.register(Players)
# class PlayersAdmin(admin.ModelAdmin):
#     change_list_template = "admin/change_list.html"

#     def get_urls(self):
#         urls = super().get_urls()
#         new_urls = [path("import-csv/", self.upload_csv)]
#         return new_urls + urls

#     def upload_csv(self, request):
#         # TODO: If records exist, bulk_update
#         if request.method == "POST":
#             csv_file = request.FILES["csv_file"]

#             df = pd.read_csv(csv_file, dtype={"current_team_id": pd.Int16Dtype()})
#             df.drop(df[
#                 pd.isna(df["current_team_id"]) or df["status"].isin(["CUT", "RET", "", "E14", "E01"])
#                 ].index, inplace=True)
#             df.rename(columns={"current_team_id": "current_team_id_id"}, inplace=True)

#             players = list()
#             for idx, row in df.iterrows():
#                 row.drop(labels=row[row.isnull()].keys(), inplace=True)
#                 players.append(Players(**row.to_dict()))

#             Players.objects.bulk_create(players)

#             self.message_user(request, "Your csv file has been imported")

#         form = ImportCSVForm()
#         data = {"form": form}

#         return render(request, "admin/import-csv.html", data)


# @admin.register(PlayerIDs)
# class PlayerIDsAdmin(admin.ModelAdmin):
#     change_list_template = "admin/change_list.html"

#     def get_urls(self):
#         urls = super().get_urls()
#         new_urls = [path("import-csv/", self.upload_csv)]
#         return new_urls + urls

#     def upload_csv(self, request):
#         # TODO: If records exist, bulk_update
#         if request.method == "POST":
#             csv_file = request.FILES["csv_file"]

#             df = pd.read_csv(csv_file)
#             player_ids = (PlayerIDs(**record) for record in df.to_dict("records"))
#             PlayerIDs.objects.bulk_create(player_ids)

#             self.message_user(request, "Your csv file has been imported")

#         form = ImportCSVForm()
#         data = {"form": form}

#         return render(request, "admin/import-csv.html", data)
