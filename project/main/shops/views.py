from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


# ITEMS VIEW
class ItemListView(APIView):
    def get(self,request):
        items = Item.objects.all()
        serializer = ItemListSerializer(items, many=True)
        return Response(serializer.data)

class ItemDetailView(APIView):
    def get(self,request, pk):
        item = Item.objects.get(id = pk)
        serializer = ItemDetailSerializer(item)
        return Response(serializer.data)

class CategoryListView(APIView):

    def get(self,request):
        categories = Category.objects.all()
        serializer = CategoryListSerializer(categories,many=True)
        return Response(serializer.data)

class CategoryDetailView(APIView):

    def get(self,request, pk):
        category = Category.objects.get(id = pk)
        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data)



