from rest_framework import serializers
from .models import *

class CategoryListSerializer(serializers.ModelSerializer): # для категории листов
    class Meta:
        model = Category
        fields = ('id', 'title')

class PriceSerializer(serializers.ModelSerializer): # для цен
    price = serializers.SlugRelatedField(slug_field='price', read_only=True)
    shop_id = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Price
        fields = ('price','shop_id')

class ItemListSerializer(serializers.ModelSerializer): # для листов товаров
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)

    def get_price(self, obj):
        try:
            price = serializers.SlugRelatedField(slug_field='price', read_only=True, many=True)
            # price = obj.
            serializer = PriceSerializer(price)
            return serializer.data
        except Exception as ex:
            return None


    class Meta:
        model = Item
        fields = ('id','title','price', 'category')



class ItemDetailSerializer(serializers.ModelSerializer):   # для каждого товара
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Item
        fields = '__all__'



class CategoryDetailSerializer(serializers.ModelSerializer): # для каждой категории
    item = ItemListSerializer(read_only=True)
    class Meta:
        model = Category
        fields = '__all__'


