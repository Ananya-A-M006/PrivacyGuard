from rest_framework import serializers


class ScanSerializer(serializers.Serializer):

    url = serializers.URLField(
        required=True,
        help_text="Website URL to scan"
    )