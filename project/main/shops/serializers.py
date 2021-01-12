from rest_framework import serializers
from .models import *



class PriceSerializer(serializers.ModelSerializer): # для цен
    price = serializers.SlugRelatedField(slug_field='price', read_only=True)
    shop_id = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Price
        fields = ('price','shop_id')

class ShopListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"

class ItemListSerializer(serializers.ModelSerializer): # для листов товаров
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    price = serializers.SlugRelatedField(slug_field='price',read_only=True, many=True)

    class Meta:
        model = Item
        fields = "__all__"



class ItemDetailSerializer(serializers.ModelSerializer):   # для каждого товара
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    class Meta:
        model = Item
        fields = '__all__'




class CategoryListSerializer(serializers.ModelSerializer): # для категории листов
    class Meta:
        model = Category
        fields = ('id', 'title')


class CategoryDetailSerializer(serializers.ModelSerializer): # для каждой категории
    item = ItemListSerializer(read_only=True)
    class Meta:
        model = Category
        fields = '__all__'

class CategoryMinPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    # price = serializers.SerializerMethodField()
    # def get_price(self, obj):
    #     try:
    #         price = obj.price.order_by('price').first()
    #         serializer = PriceSerializer(price)
    #         return serializer.data['price']
    #     except Exception as ex:
    #         return ex




