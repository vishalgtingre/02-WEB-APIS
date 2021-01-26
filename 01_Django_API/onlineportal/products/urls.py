from django.urls import path
from .views import ProductDetailView,ProductListView

urlpatterns = [
    path("products/<int:pk>/",ProductDetailView.as_view(),name = "Product_Detail"),
    path("", ProductListView.as_view(), name = "Product_List")
]
