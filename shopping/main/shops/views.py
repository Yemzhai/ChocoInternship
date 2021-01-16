from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import *
from .utils import ObjectListMixin, ObjectDetailMixin


# ITEMS VIEW
class ItemListView(ObjectListMixin, APIView):
    model = Item
    serializer = ItemListSerializer


class ItemDetailView(ObjectDetailMixin, APIView):
    model = Item
    serializer = ItemDetailSerializer


# CATEGORIES VIEW
class CategoryListView(ObjectListMixin, APIView):
    model = Category
    serializer = CategoryListSerializer


class CategoryDetailView(ObjectDetailMixin, APIView):
    model = Category
    serializer = CategoryDetailSerializer


class CategoryMinPriceView(ObjectListMixin, APIView):
    model = Category
    serializer = CategoryMinPriceSerializer

