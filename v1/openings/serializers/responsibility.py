from rest_framework import serializers

from ..models.responsibility import Responsibility


class ResponsibilitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = 'pk', 'title', 'created_date', 'modified_date'
        model = Responsibility
        read_only_fields = 'created_date', 'modified_date'
