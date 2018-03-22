from rest_framework import serializers

from .models import Painting


class PaintingSerializer(serializers.ModelSerializer):
    url = serializers.URLField(source='image.url')

    class Meta:
        model = Painting
        fields = ('id', 'url', 'cost', 'name',
                  'height', 'width', 'longitude', 'latitude',)
