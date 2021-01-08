from rest_framework import serializers
from .models import Shop


class ShopListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop


class ShopDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop

