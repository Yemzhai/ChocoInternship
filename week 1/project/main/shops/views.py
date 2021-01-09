from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# CATEGORIES VIEW
class CategoryListView(APIView):
    def get_all(self,request):
        categories = Category.objects.all()
        serializer = CategoryListSerializer(categories, many=True)
        return Response(serializer.data)

class CategoryDetailView(APIView):
    def get_datail(self,request,pk):
        category = Category.objects.get(id = pk)
        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data)

# ITEMS VIEW
class ItemListView(APIView):
    def get_all(self,request):
        devices = Item.objects.all()
        serializer = ItemListSerializer(devices, many=True)
        return Response(serializer.data)

class ItemDetailView(APIView):
    def get_detail(self,request,pk):
        item = Item.objects.get(id = pk)
        serializer = ItemDetailSerializer(item)
        return Response(serializer.data)




