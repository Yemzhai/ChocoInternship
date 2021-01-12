from django.urls import path, include
from .views import *

urlpatterns = [
    path('items/', ItemListView.as_view()),
    path('item/<int:pk>/', ItemDetailView.as_view()),
    path('categories/',CategoryListView.as_view()),
    path('category/<int:pk>/',CategoryDetailView.as_view()),
    path('category/minprice/', CategoryMinPriceView.as_view()),

]
