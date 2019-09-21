from rest_framework import serializers
from reduce.models import MinUrl


class MinUrlSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    url = serializers.URLField(required=True, allow_blank=True, max_length=2048)

    def create(self, validated_data):
        """
        Create and return a new `MinUrl` instance, given the validated data.
        """
        return MinUrl.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `MinUrl` instance, given the validated data.
        """
        instance.url = validated_data.get('url', instance.title)
        instance.save()
        return instance