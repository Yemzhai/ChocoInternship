from django.urls import path, include
from .views import *

urlpatterns = [
    path('category/', CategoryListView.as_view()),
    path('item/', ItemListView.as_view()),
    path('item/<int:pk>/', ItemDetailView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
]
