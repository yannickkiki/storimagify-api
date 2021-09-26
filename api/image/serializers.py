from rest_framework import serializers

from api.image.models import Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        write_fields = ('url',)
        fields = ('id',) + write_fields
