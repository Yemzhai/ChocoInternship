from django.urls import path, include
from .views import ShopsListView, ShopDetailView

urlpatterns = [
    path('all/', ShopsListView.as_view()),
    path('shop/detail/<int:pk>', ShopDetailView.as_view()),
]
