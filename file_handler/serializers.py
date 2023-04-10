from rest_framework import serializers
from .models import FileTemplate


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileTemplate
        fields = "__all__"
        read_only_fields = ("id",)