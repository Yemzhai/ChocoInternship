from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


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




