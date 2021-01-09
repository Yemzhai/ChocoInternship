from rest_framework import serializers
from .models import *

class CategoryListSerializer(serializers.ModelSerializer): # для категории листов
    class Meta:
        model = Category


class PriceSerializer(serializers.ModelSerializer): # для цен
    class Meta:
        model = Price
        fields = ('price','date')

class ItemListSerializer(serializers.ModelSerializer): # для листов товаров
    price = serializers.SerializerMethodField()
    def get_price(self, obj):
        try:
            price = obj.price.latest('date')
            serializer = PriceSerializer(price)
            return serializer.data
        except Exception as ex:
            return None

    class Meta:
        model = Item
        fields = ('id','name','price')

class ItemDetailSerializer(serializers.ModelSerializer):   # для каждого товара
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    shop = serializers.SlugRelatedField(slug_field='title', read_only=True)
    price = PriceSerializer(many=True)

    class Meta:
        model = Item


class CategoryDetailSerializer(serializers.ModelSerializer): # для каждой категории
    item = ItemListSerializer(many=True)
    class Meta:
        model = Category


