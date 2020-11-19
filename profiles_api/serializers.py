from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Creating serialzers without having a model."""
    name = serializers.CharField(max_length=10)
