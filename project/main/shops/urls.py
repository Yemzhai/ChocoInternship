from django.urls import path, include
from .views import *

urlpatterns = [
    path('items/', ItemListView.as_view(), name='items_url'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail_url'),
    path('categories/',CategoryListView.as_view(), name='categories_url'),
    path('category/<int:pk>/',CategoryDetailView.as_view(), name='category_detail_url'),
    path('category/minprice/', CategoryMinPriceView.as_view(), name='minprice_url'),

]
