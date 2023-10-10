from rest_framework import serializers


class FilteredListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(**self.context["request"])
        return super().to_representation(data)