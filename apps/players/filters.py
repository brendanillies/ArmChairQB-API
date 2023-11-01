import django_filters

from .models import Roster, DepthChart


class PlayerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name="gsis_id__player_name", lookup_expr="contains", label="name"
    )


class RosterFilter(PlayerFilter):
    class Meta:
        model = Roster
        fields = ["name", "season", "week", "team"]


class DepthChartFilter(PlayerFilter):
    class Meta:
        model = DepthChart
        fields = ["name", "season", "week", "team"]
