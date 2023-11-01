import django_filters

from .models import Teams


class TeamFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="team_name", lookup_expr="contains")
    abbr = django_filters.CharFilter(field_name="team", lookup_expr="contains")
    nickname = django_filters.CharFilter(field_name="team_nick", lookup_expr="contains")
    division = django_filters.CharFilter(field_name="team_division")

    class Meta:
        model = Teams
        fields = ["name", "abbr", "nickname", "division"]
