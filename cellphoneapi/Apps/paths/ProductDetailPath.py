from django.urls import path
from ..api.ProductDetailApi import ProductDetailListView, ProductDetailApiView

urlpatterns = [
    path('', ProductDetailListView.as_view()),
    path('<int:id>', ProductDetailApiView.as_view())
]
