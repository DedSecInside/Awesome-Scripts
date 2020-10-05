from rest_framework import serializers
from .models import post
from .models import category
class postserializer(serializers.ModelSerializer):
    class Meta:
        model = post

        fields = "__all__"
class categoryserializers(serializers.ModelSerializer):
    class Meta:
        model = category

        fields = "__all__"
