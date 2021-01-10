from django.urls import path, include
from .views import *

urlpatterns = [
    path('items/', ItemListView.as_view()),
    path('item/<int:pk>/', ItemDetailView.as_view()),
]
