from django.contrib import admin
from django.forms import Form, FileField
from django.urls import path
from django.shortcuts import render
from .models import Teams
import pandas as pd


class ImportCSVForm(Form):
    csv_file = FileField()


@admin.register(Teams)
class TeamsAdmin(admin.ModelAdmin):
    change_list_template = "admin/teams/change_list.html"
    list_display = ["team", "team_name", "team_division"]
    search_fields = [
        "team__icontains",
        "team_name__icontains",
        "team_division__icontains",
    ]

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path("import-csv/", self.upload_csv)]
        return new_urls + urls

    def upload_csv(self, request):
        # TODO: If records exist, bulk_update
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]

            df = pd.read_csv(csv_file)
            teams = (Teams(**record) for record in df.to_dict("records"))
            Teams.objects.bulk_create(teams)

            self.message_user(request, "Your csv file has been imported")

        form = ImportCSVForm()
        data = {"form": form}

        return render(request, "admin/teams/import-csv.html", data)
