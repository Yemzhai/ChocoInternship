from django.shortcuts import render
from .models import Shop
from rest_framework import generics
from .serializers import ShopDetailSerializer, ShopListSerializer


class ShopsListView(generics.ListAPIView):
    serializer_class = ShopListSerializer
    queryset = Shop.objects.all()


class ShopDetailView(generics.RetrieveAPIView):
    serializer_class = ShopDetailSerializer
    queryset = Shop.objects.all()
