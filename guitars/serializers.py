from rest_framework import serializers
from guitars.models import Guitars


class GuitarsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Guitars
        fields = "__all__"
