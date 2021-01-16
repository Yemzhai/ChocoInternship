from rest_framework.views import APIView
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


# MAX and MIN PRICE IN CATEGORIES
class CategoryMinPriceView(ObjectListMixin, APIView):
    model = Category
    serializer = CategoryMinPriceSerializer


class CategoryMaxPriceView(ObjectListMixin, APIView):
    model = Category
    serializer = CategoryMaxPriceSerializer


# PRICES VIEW
class PriceListView(ObjectListMixin, APIView):
    model = Price
    serializer = PriceSerializer
