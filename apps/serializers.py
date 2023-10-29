from rest_framework import serializers


class FilteredListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(**self.context["query_params"])
        return super().to_representation(data)


class CustomModelSerializer(serializers.ModelSerializer):

    def get_field_names(self, declared_fields, info):
        expanded_fields = super().get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields